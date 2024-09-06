import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

cell_dimensions = 10


class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_coords(self) -> tuple[int, int]:
        return (self.x, self.y)


cells = [Cell(20, 20), Cell(21, 20), Cell(22, 20)]

camera_x = 0
camera_y = 0
update_count = 0

while running:

    update_count += 1

    if update_count > 30:
        update_count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    new_cells = cells[:]

    if update_count == 0:

        dead_neighbours = {}

        for cell in cells:
            neighbours = 0

            for other_cells in cells:
                if other_cells.get_coords() == (cell.x - 1, cell.y):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x + 1, cell.y):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x, cell.y - 1):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x, cell.y + 1):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x - 1, cell.y - 1):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x + 1, cell.y + 1):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x + 1, cell.y - 1):
                    neighbours += 1
                if other_cells.get_coords() == (cell.x - 1, cell.y + 1):
                    neighbours += 1

            current_cell = (cell.x + 1, cell.y)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x - 1, cell.y)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x, cell.y + 1)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x, cell.y - 1)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x + 1, cell.y + 1)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x - 1, cell.y - 1)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x - 1, cell.y + 1)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            current_cell = (cell.x + 1, cell.y - 1)
            if current_cell not in dead_neighbours:
                dead_neighbours[current_cell] = 1
            else:
                dead_neighbours[current_cell] += 1

            if neighbours < 2:
                new_cells.remove(cell)
            if neighbours > 3:
                new_cells.remove(cell)

        for dead_cell in dead_neighbours:
            if dead_neighbours[dead_cell] == 3:
                new_cells.append(Cell(dead_cell[0], dead_cell[1]))

        cells = new_cells[:]

    for cell in cells:
        pygame.draw.rect(
            screen,
            "white",
            pygame.Rect(
                cell.x * cell_dimensions + camera_x,
                cell.y * cell_dimensions + camera_y,
                cell_dimensions,
                cell_dimensions,
            ),
        )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        camera_y += 300 * dt
    if keys[pygame.K_s]:
        camera_y -= 300 * dt
    if keys[pygame.K_a]:
        camera_x += 300 * dt
    if keys[pygame.K_d]:
        camera_x -= 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
