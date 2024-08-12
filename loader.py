import argparse
import envInit
#import downloadNeccesaryLibs
import runGUI


def main():
    
    env_name = "cellpose_env"
    python_version = "3.8"
    
    # Initialize Conda environment
    condaPath = envInit.get_conda_path()
    if not envInit.is_conda_installed():
        try:
            envInit.download_and_install_conda()
        except Exception as e:
            print(f"Error during Conda installation: {e}")
            sys.exit(1)

    if not envInit.environment_exists(env_name):
        envInit.create_conda_env(env_name, python_version)
        envInit.install_cellpose(env_name)
        
        
        envInit.install_latest_torch(env_name, use_cuda=False) #Got a little messy and is a pain to setup the other libraries again. use_cuda stays
        
        envInit.install_additional_libraries(env_name)
    else:
        print(f"Conda environment '{env_name}' already exists. Skipping environment setup.")

    # Download necessary libraries
    

    # Run the main script inside the Conda environment
    
    fullPath = f"AutomationFolder/main.py"
    
    
    runGUI.create_and_run_batch_file(env_name, fullPath, condaPath)

if __name__ == "__main__":
    main()
