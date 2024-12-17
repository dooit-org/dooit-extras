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
    forEachSystem = nixpkgs.lib.genAttrs nixpkgs.lib.systems.flakeExposed;
  in {
    # Define the overlay
    overlays.default = final: prev: {
      dooit-extras = prev.callPackage ./nix {
        dooit = dooit.packages.${final.system}.default;
      };
    };

    # Make packages available
    packages = forEachSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [self.overlays.default];
      };
    in {
      default = pkgs.dooit-extras;
    });

    # Make overlay available for home-manager or other configurations
    nixpkgs.overlays = [self.overlays.default];
  };
}
