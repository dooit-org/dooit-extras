{
  description = "Flake for Dooit Extras";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.dooit.url = "github:kraanzu/dooit?ref=develop";

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    dooit,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      python3 = pkgs.python312Packages;
    in {
      packages.default = python3.buildPythonPackage {
        pname = "dooit-extras";
        version = "0.1.0";
        src = ./.;

        format = "pyproject";

        # Dependencies for building the package
        nativeBuildInputs = with pkgs; [
          poetry
          dooit.packages.${system}.default
        ];

        # Dependencies for runtime and development
        buildInputs = with python3; [
          textual
          poetry-core
        ];

        doCheck = true; # Enable tests
        checkInputs = with python3; [
          pytest
          pytest-asyncio
          coverage
          faker
        ];
      };

      # Development environment
      devShell = pkgs.mkShell {
        name = "dooit-extras-dev";
        buildInputs =
          (with python3; [
            ruff
            pre-commit-hooks
            textual-dev
            pytest
            coverage
            faker
          ])
          ++ [pkgs.bun];

        shellHook = ''
          cd site
          ${pkgs.bun}/bin/bun install
          cd ..
        '';
      };
    });
}
