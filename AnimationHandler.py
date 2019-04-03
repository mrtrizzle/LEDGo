
import glob, subprocess, os
import psutil



class AnimationHandler(object):
    
    def __init__(self):
        self.script_path = "animations/"
        self.scripts = self.lookup_animation_scripts()
        self.script_names = self.strip_script_names(self.scripts)
        self.active_script = None
        print("AnimationHandler loaded with {} available scripts.".format(len(self.scripts)))

    def lookup_animation_scripts(self):
        PATH = self.script_path+"*.py"
        return glob.glob(PATH)

    def start_animation_by_name(self, animation_name):
        self.kill_all_child_processes()
        self.active_script = subprocess.Popen(['python', os.path.join(
            self.script_path, animation_name+".py")])
        return True

    def kill_all_child_processes(self):
        if self.active_script is not None:
            self.active_script.terminate()
        #current_process = psutil.Process()
        #children = current_process.children(recursive=True)
        #for child in children:
        #    child.kill()

    
    def strip_script_names(self, scripts):
        return [os.path.splitext(os.path.basename(s))[0] for s in scripts if "opc.py" not in s]

