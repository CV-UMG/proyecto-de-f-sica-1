import pygame
import sys

pygame.init()

# =========================
# CONFIG
# =========================
W, H = 900, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simulador Newton Simple")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# =========================
# INPUT SIMPLE
# =========================
class Campo:
    def __init__(self, x, y, texto, valor):
        self.rect = pygame.Rect(x, y, 80, 30)
        self.nombre = texto
        self.texto = str(valor)
        self.activo = False

    def draw(self):
        color = (0,150,255) if self.activo else (0,0,0)
        pygame.draw.rect(screen, (255,255,255), self.rect)
        pygame.draw.rect(screen, color, self.rect, 2)

        label = font.render(self.nombre, True, (0,0,0))
        screen.blit(label, (self.rect.x, self.rect.y - 25))

        txt = font.render(self.texto, True, (0,0,0))
        screen.blit(txt, (self.rect.x + 5, self.rect.y + 5))

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.activo = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.activo:
            if event.key == pygame.K_BACKSPACE:
                self.texto = self.texto[:-1]
            else:
                self.texto += event.unicode

    def valor(self):
        try:
            return float(self.texto)
        except:
            return 0

# =========================
# CAMPOS
# =========================
peso1 = Campo(50, 80, "F1 (N)", 10)
peso2 = Campo(150, 80, "F2 (N)", 5)

masa1 = Campo(50, 200, "m1", 3)
masa2 = Campo(150, 200, "m2", 4)
fuerza = Campo(250, 200, "F", 20)

campos = [peso1, peso2, masa1, masa2, fuerza]

# =========================
# ESTADO
# =========================
modo = 1
vel = 0
pos = 0
pausa = False

# =========================
# LOOP
# =========================
while True:

    import pygame
    import sys

    pygame.init()

    W, H = 950, 550
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Simulador Newton")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 26)

    g = 9.8


    # =========================
    # BOTON
    # =========================
    class Boton:
        def __init__(self, x, y, w, h, texto):
            self.rect = pygame.Rect(x, y, w, h)
            self.texto = texto

        def draw(self):
            pygame.draw.rect(screen, (200, 200, 200), self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
            txt = font.render(self.texto, True, (0, 0, 0))
            screen.blit(txt, (self.rect.x + 10, self.rect.y + 8))

        def click(self, pos):
            return self.rect.collidepoint(pos)


    # =========================
    # INPUT
    # =========================
    class Campo:
        def __init__(self, x, y, nombre, valor):
            self.rect = pygame.Rect(x, y, 80, 30)
            self.nombre = nombre
            self.texto = str(valor)
            self.activo = False

        def draw(self):
            color = (0, 150, 255) if self.activo else (0, 0, 0)
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
            pygame.draw.rect(screen, color, self.rect, 2)

            screen.blit(font.render(self.nombre, True, (0, 0, 0)), (self.rect.x, self.rect.y - 18))
            screen.blit(font.render(self.texto, True, (0, 0, 0)), (self.rect.x + 5, self.rect.y + 5))

        def handle(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.activo = self.rect.collidepoint(event.pos)

            if event.type == pygame.KEYDOWN and self.activo:
                if event.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                elif event.unicode.isdigit() or event.unicode == ".":
                    self.texto += event.unicode

        def valor(self):
            try:
                return float(self.texto)
            except:
                return 0


    # =========================
    # UI ELEMENTOS
    # =========================
    btn_polea = Boton(20, 20, 120, 40, "Polea")
    btn_tercera = Boton(160, 20, 140, 40, "Tercera Ley")
    btn_reset = Boton(320, 20, 120, 40, "Reiniciar")

    # =========================
    # INPUTS ALINEADOS (MISMA ALTURA)
    # =========================
    Y_INPUT = 260

    # Polea (izquierda)
    m1 = Campo(20, Y_INPUT, "m1", 10)
    m2 = Campo(120, Y_INPUT, "m2", 5)

    # Tercera ley (derecha)
    mA = Campo(320, Y_INPUT, "mA", 3)
    mB = Campo(420, Y_INPUT, "mB", 4)
    F = Campo(520, Y_INPUT, "F", 20)

    campos = [m1, m2, mA, mB, F]

    # =========================
    # ESTADO
    # =========================
    modo = 1
    vel = 0
    pos = 0
    pausa = False


    def reset():
        global vel, pos, pausa
        vel = 0
        pos = 0
        pausa = False


    # =========================
    # FLECHA
    # =========================
    def flecha(x1, y1, x2, y2, texto):
        pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)
        pygame.draw.circle(screen, (0, 0, 0), (x2, y2), 4)
        screen.blit(font.render(texto, True, (0, 0, 0)), (x2 + 5, y2))


    # =========================
    # LOOP
    # =========================
    while True:

        import pygame
        import sys

        pygame.init()

        W, H = 950, 550
        screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("Simulador Newton")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 26)

        g = 9.8


        # =========================
        # BOTON
        # =========================
        class Boton:
            def __init__(self, x, y, w, h, texto):
                self.rect = pygame.Rect(x, y, w, h)
                self.texto = texto

            def draw(self):
                pygame.draw.rect(screen, (200, 200, 200), self.rect)
                pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
                txt = font.render(self.texto, True, (0, 0, 0))
                screen.blit(txt, (self.rect.x + 10, self.rect.y + 8))

            def click(self, pos):
                return self.rect.collidepoint(pos)


        # =========================
        # INPUT
        # =========================
        class Campo:
            def __init__(self, x, y, nombre, valor):
                self.rect = pygame.Rect(x, y, 80, 30)
                self.nombre = nombre
                self.texto = str(valor)
                self.activo = False

            def draw(self):
                color = (0, 150, 255) if self.activo else (0, 0, 0)
                pygame.draw.rect(screen, (255, 255, 255), self.rect)
                pygame.draw.rect(screen, color, self.rect, 2)

                screen.blit(font.render(self.nombre, True, (0, 0, 0)), (self.rect.x, self.rect.y - 18))
                screen.blit(font.render(self.texto, True, (0, 0, 0)), (self.rect.x + 5, self.rect.y + 5))

            def handle(self, event):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.activo = self.rect.collidepoint(event.pos)

                if event.type == pygame.KEYDOWN and self.activo:
                    if event.key == pygame.K_BACKSPACE:
                        self.texto = self.texto[:-1]
                    elif event.unicode.isdigit() or event.unicode == ".":
                        self.texto += event.unicode

            def valor(self):
                try:
                    return float(self.texto)
                except:
                    return 0


        # =========================
        # UI ELEMENTOS
        # =========================
        btn_polea = Boton(20, 20, 120, 40, "Polea")
        btn_tercera = Boton(160, 20, 140, 40, "Tercera Ley")
        btn_reset = Boton(320, 20, 120, 40, "Reiniciar")

        Y_INPUT = 260

        # Polea
        m1 = Campo(20, Y_INPUT, "m1", 10)
        m2 = Campo(120, Y_INPUT, "m2", 5)

        # Tercera ley
        mA = Campo(320, Y_INPUT, "mA", 3)
        mB = Campo(420, Y_INPUT, "mB", 4)
        F = Campo(520, Y_INPUT, "F", 20)

        # 🔥 SEPARACIÓN DE CAMPOS
        campos_polea = [m1, m2]
        campos_tercera = [mA, mB, F]

        # =========================
        # ESTADO
        # =========================
        modo = 1
        vel = 0
        pos = 0
        pausa = False


        def reset():
            global vel, pos, pausa
            vel = 0
            pos = 0
            pausa = False


        # =========================
        # FLECHA
        # =========================
        def flecha(x1, y1, x2, y2, texto):
            pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)
            pygame.draw.circle(screen, (0, 0, 0), (x2, y2), 4)
            screen.blit(font.render(texto, True, (0, 0, 0)), (x2 + 5, y2))


        # =========================
        # LOOP
        # =========================
        while True:

            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # 🔥 SOLO INPUTS DEL MODO ACTIVO
                if modo == 1:
                    for c in campos_polea:
                        c.handle(event)
                else:
                    for c in campos_tercera:
                        c.handle(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_polea.click(event.pos):
                        modo = 1
                        reset()
                        for c in campos_polea + campos_tercera:
                            c.activo = False

                    if btn_tercera.click(event.pos):
                        modo = 2
                        reset()
                        for c in campos_polea + campos_tercera:
                            c.activo = False

                    if btn_reset.click(event.pos):
                        reset()

            screen.fill((255, 255, 255))

            btn_polea.draw()
            btn_tercera.draw()
            btn_reset.draw()

            # =========================
            # POLEA
            # =========================
            if modo == 1:

                M1 = m1.valor()
                M2 = m2.valor()

                if (M1 + M2) != 0:
                    a = ((M1 - M2) * g) / (M1 + M2)
                    T = M1 * (g - a)
                else:
                    a, T = 0, 0

                if not pausa:
                    vel += a * dt
                    pos += vel * 100 * dt
                    if abs(pos) > 120:
                        pausa = True

                pygame.draw.circle(screen, (0, 0, 0), (500, 100), 25, 2)
                pygame.draw.line(screen, (0, 0, 0), (480, 100), (480, 220 + pos), 2)
                pygame.draw.line(screen, (0, 0, 0), (520, 100), (520, 220 - pos), 2)

                pygame.draw.rect(screen, (0, 0, 255), (465, 220 + pos, 30, 30))
                pygame.draw.rect(screen, (255, 0, 0), (505, 220 - pos, 30, 30))

                flecha(480, 220 + pos, 480, 260 + pos, "W1")
                flecha(480, 220 + pos, 480, 180 + pos, "T")
                flecha(520, 220 - pos, 520, 180 - pos, "T")
                flecha(520, 220 - pos, 520, 260 - pos, "W2")

                screen.blit(font.render(f"a = {round(a, 2)}", True, (0, 0, 0)), (20, 60))
                screen.blit(font.render(f"T = {round(T, 2)}", True, (0, 0, 0)), (20, 90))

            # =========================
            # TERCERA LEY
            # =========================
            else:

                MA = mA.valor()
                MB = mB.valor()
                Fuerza = F.valor()

                if (MA + MB) != 0:
                    a = Fuerza / (MA + MB)
                    F_BA = MB * a
                else:
                    a, F_BA = 0, 0

                if not pausa:
                    vel += a * dt
                    pos += vel * 100 * dt
                    if pos > 200:
                        pausa = True

                pygame.draw.rect(screen, (0, 200, 255), (350 + pos, 350, 50, 50))
                pygame.draw.rect(screen, (255, 150, 0), (400 + pos, 350, 60, 60))

                flecha(340 + pos, 375, 300 + pos, 375, "F")
                flecha(410 + pos, 375, 450 + pos, 375, "F_BA")

                screen.blit(font.render(f"a = {round(a, 2)}", True, (0, 0, 0)), (20, 60))
                screen.blit(font.render(f"F_BA = {round(F_BA, 2)}", True, (0, 0, 0)), (20, 90))

            # =========================
            # DIBUJAR INPUTS SOLO DEL MODO
            # =========================
            if modo == 1:
                screen.blit(font.render(
                    "Problema: Dos masas cuelgan de una polea ideal.",
                    True, (0, 0, 0)), (20, 140))

                screen.blit(font.render(
                    "Ingrese m1 y m2 para calcular aceleración y tensión.",
                    True, (0, 0, 0)), (20, 170))
                for c in campos_polea:
                    c.draw()

            else:
                screen.blit(font.render(
                    "Problema: Dos bloques están en contacto.",
                    True, (0, 0, 0)), (20, 140))

                screen.blit(font.render(
                    "Ingrese masas y fuerza para calcular a y F_BA.",
                    True, (0, 0, 0)), (20, 170))
                for c in campos_tercera:
                    c.draw()

            # títulos
            screen.blit(font.render("Polea", True, (0, 0, 0)), (20, 230))
            screen.blit(font.render("Tercera Ley", True, (0, 0, 0)), (320, 230))

            pygame.display.flip()