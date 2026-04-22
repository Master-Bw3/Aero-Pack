let
  nixpkgsVer = "e6515129584048031d14f4ba61481a2254314018";
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/${nixpkgsVer}.tar.gz") { config = {}; overlays = []; };

in pkgs.mkShell {
  name = "shell";

  buildInputs = with pkgs; [
    packwiz
  ];

}