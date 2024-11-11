{
  lib,
  fetchFromGitHub,
  python311,
  dooit,
}: let
  python3 = python311;
in
  python3.pkgs.buildPythonPackage {
    pname = "dooit-extras";
    version = "0.1.0";
    pyproject = true;

    src = fetchFromGitHub {
      owner = "dooit-org";
      repo = "dooit-extras";
      rev = "main";
      hash = "sha256-FsgR/2fEC/6uxbyUm7CC0st+s4ASp0HNGBoTssEVijc=";
    };

    build-system = with python3.pkgs; [poetry-core];
    buildInputs = [dooit];

    # No tests available
    doCheck = false;

    meta = with lib; {
      description = "Extra Utilities for Dooit";
      homepage = "https://github.com/dooit-org/dooit-extras";
      changelog = "https://github.com/dooit-org/dooit-extras/blob/v${version}/CHANGELOG.md";
      license = licenses.mit;
      maintainers = with maintainers; [
        kraanzu
      ];
    };
  }
