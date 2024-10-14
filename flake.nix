{
  description = "Flake for Dooit Extras";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.dooit.url = "github:kraanzu/dooit?ref=develop";

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    dooit
  }
  :
    flake-utils.lib.eachDefaultSystem (
      system: let
        name = "dooit-extras";
        version = "0.1.0";

        pkgs = import nixpkgs {inherit system;};
        python3 = pkgs.python312Packages;

        mainPkgs = with python3; [
          textual
          poetry-core
        ];
      in {
        packages.default = python3.buildPythonPackage {
          pname = name;
          version = version;
          src = ./.;
          format = "pyproject";

          nativeBuildInputs = with pkgs; [
            poetry
            dooit.packages.${system}.default
          ];

          pythonRelaxDeps = [
            "textual"
          ];

          buildInputs = mainPkgs;

          doCheck = false; # no tests
        };

        # Deps: Devshell
        devShell = pkgs.mkShell {
          name = "dooit-extras";
          buildInputs =
            mainPkgs
            ++ (with pkgs; [
              bun
            ]);

          shellHook = ''
            cd site
            ${pkgs.bun}/bin/bun install
            cd ..
          '';
        };
      }
    );
}
