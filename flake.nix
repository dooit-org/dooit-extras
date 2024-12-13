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

    pkgsFor = forEachSystem (
      system:
        import nixpkgs {
          inherit system;
          overlays = [
            (final: prev: {
              dooit-extras = prev.callPackage ./nix {
                dooit = dooit.packages.${system}.default;
              };
            })
          ];
        }
    );
  in {
    packages = forEachSystem (system: {
      default = pkgsFor.${system}.dooit-extras;
    });
  };
}
