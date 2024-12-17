{
  description = "Flake for Dooit Extras";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    dooit.url = "github:dooit-org/dooit";
  };

  outputs = {
    self,
    nixpkgs,
    dooit,
    ...
  }: let
    forEachSystem = nixpkgs.lib.genAttrs nixpkgs.lib.platforms.all;
  in {
    overlays.default = final: prev: {
      dooit-extras = prev.callPackage ./nix {
        dooit = dooit.packages.${prev.system}.default;
      };
    };

    packages = forEachSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [self.overlays.default];
      };
    in {
      default = pkgs.dooit-extras;
    });
  };
}
