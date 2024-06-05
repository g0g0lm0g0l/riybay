from raylib import *

HIGHT=1200
WIDTH=800 

def main():
    InitWindow(HIGHT, WIDTH, b"Asteroids")
    SetTargetFPS(60)
    posX_rect = int(HIGHT/2-HIGHT/10/2)
    posY_rect = int(WIDTH/2-WIDTH/10/2)

    i = 0
    while not WindowShouldClose():
        BeginDrawing()
        ClearBackground(BLACK)
        if IsKeyDown(KEY_Q):
            CloseWindow()
        if IsKeyDown(KEY_LEFT):
            posX_rect -= 10
        if IsKeyDown(KEY_RIGHT):
            posX_rect += 10
        if IsKeyDown(KEY_UP):
            posY_rect -= 10
        if IsKeyDown(KEY_DOWN):
            posY_rect += 10
        if IsKeyPressed(KEY_SPACE):
            for i in range(posY_rect, 0, -1):
                DrawRectangleGradientH(int(posX_rect+WIDTH/10/4), i, int(WIDTH/20), int(HIGHT/20), RED, GREEN)
        i += 1
        DrawTriangle([posX_rect-WIDTH/3+int(WIDTH/20), HIGHT/3], [posX_rect+int(WIDTH/20), posY_rect], [posX_rect+WIDTH/3, HIGHT/3], MAGENTA)
        DrawPoly([int(WIDTH/4+500)-GetFPS(), int(HIGHT/4)-GetFPS()], 10, 50.0+i, 0.0, WHITE)
        DrawText((str(GetFPS())).encode("ascii"), 10, 10, 20, SKYBLUE)
        DrawCircleGradient(int(WIDTH/3)+GetFPS(), int(HIGHT/3)-GetFPS(), 100.0+i, RED, YELLOW)
        DrawEllipse(int(WIDTH/5)+GetFPS(), int(HIGHT/5+300)+GetFPS(), 40.0, 60.0+i, VIOLET)
        DrawRectangleGradientH(posX_rect, posY_rect, int(WIDTH/10), int(HIGHT/10), YELLOW, GREEN)
        if i == 100:
            i = 0
        EndDrawing()


if __name__ == "__main__":
    main()
