from graphics_shim import ConsoleGraphics

cg = ConsoleGraphics()
with cg:
    cg.line((10,15), (10, 20), cg.RED)
    cg.line((11,15), (16, 15), cg.GREEN)

    cg.num(0, (0, 0), cg.CYAN, cg.BG)
    cg.num(1, (0, 5), cg.CYAN, cg.BG)
    cg.num(5, (0, 10), cg.CYAN, cg.BG)
    input()
