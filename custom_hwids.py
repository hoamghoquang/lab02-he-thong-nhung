Import("env")
board_config = env.BoardConfig()
board_config.update("build.hwids", [["0x0483", "0xDF11"]])