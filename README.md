# Domain Artifact Infrastructure

Infrastructure layer for [pythoneda-shared-pythoneda](https://github.com/pythoneda-shared-pythoneda "pythoneda-shared-pythoneda")/[domain-artifact](https://github.com/pythoneda-shared-pythoneda/domain-artifact "domain-artifact").

## How to declare it in your flake

Check the latest tag of the artifact repository: [https://github.com/pythoneda-shared-pythoneda/domain-artifact-infrastructure-artifact/tags](https://github.com/pythoneda-shared-pythoneda/domain-artifact-infrastructure-artifact/tags) and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-pythoneda-domain-artifact-infrastructure = {
      [optional follows]
      url =
        "github:pythoneda-shared-pythoneda/domain-artifact-infrastructure/[version]?dir=domain-artifact-infrastructure";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [nixpkgs](https://github.com/nixos/nixpkgs "nixpkgs") and [flake-utils](https://github.com/numtide/flake-utils "flake-utils").

Use the specific package depending on your system (one of `flake-utils.lib.defaultSystems`) and Python version:

- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-infrastructure-python38` 
- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-infrastructure-python39` 
- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-infrastructure-python310` 
- `#packages.[system].pythoneda-shared-pythoneda-domain-artifact-infrastructure-python311` 

The Nix flake is under the 
[domain-artifact-infrastructure](https://github.com/pythoneda-shared-pythoneda/domain-artifact-infrastructure-artifact/tree/main/domain-artifact-infrastructure "domain-artifact-infrastructure") folder.
