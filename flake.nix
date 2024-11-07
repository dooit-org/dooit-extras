{
  description = "Flake for Dooit Extras";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    dooit.url = "github:kraanzu/dooit/develop";
  };

  outputs = {
    self,
    nixpkgs,
    dooit,
    ...
  }: let
    forEachSystem = nixpkgs.lib.genAttrs nixpkgs.lib.platforms.all;

    pkgsFor = forEachSystem (
      system:
        import nixpkgs {
          inherit system;
          overlays = [dooit.overlay];
        }
    );

    packageFor = system: pkgsFor.${system}.callPackage ./nix {dooit = dooit.packages.${system}.default;};
  in {
    packages = forEachSystem (
      system: {
        default = packageFor system;
      }
    );

    overlay = final: prev: {
      dooit-extras = packageFor final.system;
    };
  };
}
