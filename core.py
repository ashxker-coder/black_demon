import importlib

class BlackDemon:
    def __init__(self, use_tor: bool = False):
        """
        Core of the Black Demon framework.
        Responsible for loading and running modules.
        """
        self.use_tor = use_tor
        if use_tor:
            print("[*] Tor mode enabled - modules should route traffic through Tor if supported.")
        else:
            print("[*] Running without Tor")

    def run_module(self, module_name: str, target: str):
        """
        Load and run a module from the 'modules' folder.
        
        :param module_name: The name of the module (e.g., portscan, httpcheck, info).
        :param target: The target (IP or domain).
        """
        try:
            module = importlib.import_module(f"modules.{module_name}")
            if hasattr(module, "run"):
                print(f"[*] Launching module: {module_name}")
                module.run(target, self.use_tor)
            else:
                print(f"[!] Module '{module_name}' does not define a run() function")
        except ModuleNotFoundError:
            print(f"[!] Module '{module_name}' not found in the 'modules' folder")
        except Exception as e:
            print(f"[!] Error while running module '{module_name}': {e}")
