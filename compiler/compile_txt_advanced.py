import os
import glob

def compile_txt_files(input_folder, output_file, add_separators=True, include_filenames=True):
    """
    Compile all .txt files in a folder into one super .txt file in alphabetical order.
    
    Args:
        input_folder (str): Path to the folder containing .txt files
        output_file (str): Path for the output compiled .txt file
        add_separators (bool): Whether to add separators between files
        include_filenames (bool): Whether to include original filenames
    """
    
    # Get all .txt files in the folder, sorted alphabetically
    txt_files = sorted(glob.glob(os.path.join(input_folder, "*.txt")))
    
    if not txt_files:
        print(f"No .txt files found in {input_folder}")
        return False
    
    print(f"Found {len(txt_files)} .txt files to compile:")
    for file in txt_files:
        print(f"  - {os.path.basename(file)}")
    
    total_files = 0
    total_chars = 0
    
    # Compile all files into one
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for i, txt_file in enumerate(txt_files):
                try:
                    with open(txt_file, 'r', encoding='utf-8') as infile:
                        # Add separator and filename if requested
                        if add_separators and i > 0:
                            outfile.write("\n\n" + "="*50 + "\n\n")
                        
                        if include_filenames:
                            outfile.write(f"File: {os.path.basename(txt_file)}\n")
                            if add_separators:
                                outfile.write("-" * 30 + "\n\n")
                        
                        # Write the content of the file
                        content = infile.read()
                        outfile.write(content)
                        
                        # Update statistics
                        total_files += 1
                        total_chars += len(content)
                        
                        print(f"✓ Processed: {os.path.basename(txt_file)} ({len(content)} characters)")
                        
                except UnicodeDecodeError:
                    print(f"Warning: UTF-8 encoding issue with {txt_file}, trying latin-1...")
                    try:
                        with open(txt_file, 'r', encoding='latin-1') as infile:
                            content = infile.read()
                            outfile.write(content)
                            total_files += 1
                            total_chars += len(content)
                            print(f"✓ Processed (latin-1): {os.path.basename(txt_file)}")
                    except Exception as e:
                        print(f"Error reading {txt_file}: {e}")
                
                except Exception as e:
                    print(f"Error reading {txt_file}: {e}")
        
        print(f"\n✅ Successfully compiled {total_files} files")
        print(f"📄 Total characters: {total_chars:,}")
        print(f"💾 Output file: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        return False

# ===== HARDCODED CONFIGURATION - MODIFY THESE VALUES =====
INPUT_FOLDER = r"./"  # Your input folder path
OUTPUT_FILE = r"./5_day_workout_compiled.tx"  # Your output file path
ADD_SEPARATORS = True  # Set to False to remove separators between files
INCLUDE_FILENAMES = False  # Set to False to remove filename headers

# ===== PATH EXAMPLES =====
# Windows: r"C:\Users\Name\folder" or "C:/Users/Name/folder"
# Mac/Linux: "/Users/Name/folder" or "/home/name/folder"
# Relative path: "./folder_name" or "../parent_folder"

if __name__ == "__main__":
    print("=== TXT File Compiler ===")
    print(f"Input folder: {INPUT_FOLDER}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Add separators: {ADD_SEPARATORS}")
    print(f"Include filenames: {INCLUDE_FILENAMES}")
    print("=" * 40)
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(OUTPUT_FILE)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Run the compilation
    success = compile_txt_files(
        input_folder=INPUT_FOLDER,
        output_file=OUTPUT_FILE,
        add_separators=ADD_SEPARATORS,
        include_filenames=INCLUDE_FILENAMES
    )
    
    if success:
        print("\n🎉 Compilation completed successfully!")
    else:
        print("\n❌ Compilation failed!")