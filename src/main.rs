use dirs;
use std::{
    fs,
    path::{Path, PathBuf},
};

fn main() -> Result<(), String> {
    let downloads_path_buffer_option = dirs::download_dir();
    let downloads_path_buffer = match downloads_path_buffer_option {
        Some(pb) => pb,
        None => return Err(String::from("Unable to create path buffer")),
    };

    let downloads_directory_path = downloads_path_buffer.as_path();
    let read_dir_result = fs::read_dir(downloads_directory_path);

    let read_dir = match read_dir_result {
        Ok(read_dir) => read_dir,
        Err(e) => return Err(e.to_string()),
    };

    read_dir
        .filter_map(|dir_entry| match dir_entry {
            Ok(de) => {
                let directory_entry_path_buffer: PathBuf = de.path();
                if directory_entry_path_buffer.is_file() {
                    return Some(directory_entry_path_buffer);
                }
                return None;
            }
            Err(_e) => None,
        })
        .for_each(|file_path| {
            let file_extension_option = file_path.extension();
            println!("Working on {}", file_path.clone().to_str().unwrap());
            if file_extension_option.is_some() {
                let file_extension = file_extension_option.unwrap();
                println!("File extension is {}", file_extension.to_str().unwrap());
                let directory_path_for_extension = downloads_path_buffer.join(file_extension);
                println!(
                    "Directory Path {}",
                    directory_path_for_extension.clone().to_str().unwrap()
                );
                if !directory_path_for_extension.exists() {
                    let extension_dir_path = directory_path_for_extension.as_path();
                    println!(
                        "Creating Directory {}",
                        extension_dir_path.to_str().unwrap()
                    );
                    match fs::create_dir(extension_dir_path) {
                        Err(e) => println!("Failed to create directory: {}", e.to_string()),
                        Ok(_) => println!("Directory Created!"),
                    };
                }
                let new_file_path =
                    directory_path_for_extension.join(Path::new(file_path.file_name().unwrap()));

                match fs::rename(file_path.as_path(), new_file_path) {
                    Err(e) => println!("Failed to move file: {}", e.to_string()),
                    Ok(_) => println!("File moved!"),
                };
            }
        });
    Ok(())
}
