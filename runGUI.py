import subprocess
import sys

def run_script_in_conda_env(env_name, script_path, conda_executable):
    # Command to run the script in the specified Conda environment
    command = f'{conda_executable} run -n {env_name} python {script_path}'
    
    try:
        print(f"Running script '{script_path}' in Conda environment '{env_name}'...")
        # Open a new Command Prompt window and run the command
        subprocess.run(['start', 'cmd', '/k', command], shell=True)
        print("Command Prompt window opened successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while opening Command Prompt window: {e}")
        sys.exit(1)

def main():
    env_name = "cellpose_env"  
    script_path = "path_to_your_python_script.py"  
    conda_executable = "conda"  

    run_script_in_conda_env(env_name, script_path, conda_executable)

if __name__ == "__main__":
    main()
