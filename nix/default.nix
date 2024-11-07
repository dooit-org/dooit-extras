{
  lib,
  fetchFromGitHub,
  python311,
  dooit,
}: let
  python3 = python311;
in
  python3.pkgs.buildPythonApplication rec {
    pname = "dooit-extras";
    version = "0.1.0";
    pyproject = true;

    src = fetchFromGitHub {
      owner = "dooit-org";
      repo = "dooit-extras";
      rev = "main";
      hash = "sha256-N0r37iEj0P/qLBFG9bGPUPjw31Wk9kA+rrZd59Yrxd4=";
    };

    build-system = with python3.pkgs; [poetry-core];
    buildInputs = [dooit];
    propagatedBuildInputs = [];

    # No tests available
    doCheck = false;

    pythonRelaxDeps = [
      "tzlocal"
      "textual"
    ];

    meta = with lib; {
      description = "Extra Utilities for Dooit";
      homepage = "https://github.com/dooit-org/dooit-extras";
      changelog = "https://github.com/dooit-org/dooit-extras/blob/main/CHANGELOG.md"; # TODO: change to version
      license = licenses.mit;
      maintainers = with maintainers; [
        kraanzu
      ];
    };
  }
