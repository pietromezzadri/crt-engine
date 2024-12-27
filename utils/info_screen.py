from backend.renderer import Renderer
from backend.font import Font


class InfoScreen:
    def __init__(self, renderer, font) -> None:
        self.fps = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.renderer: Renderer = renderer
        self.font: Font = font
        self.show = False
        self.components = []

    def display_info(self, fps):
        left_up_corner = self.font.render_text(
            f"({self.renderer.x_start:.1f}, {self.renderer.y_start:.1f})",
            "main",
            (150, 50, 50),
        )
        right_up_corner = self.font.render_text(
            f"({self.renderer.x_end:.1f}, {self.renderer.y_start:.1f})",
            "main",
            (150, 50, 50),
        )
        left_down_corner = self.font.render_text(
            f"({self.renderer.x_start:.1f}, {self.renderer.y_end:.1f})",
            "main",
            (150, 50, 50),
        )
        right_down_corner = self.font.render_text(
            f"({self.renderer.x_end:.1f}, {self.renderer.y_end:.1f})",
            "main",
            (150, 50, 50),
        )

        self.renderer.render_to_screen(left_up_corner, 10, 10)
        self.renderer.render_to_screen(right_up_corner, self.renderer.width - 230, 10)
        self.renderer.render_to_screen(left_down_corner, 10, self.renderer.height - 50)
        self.renderer.render_to_screen(
            right_down_corner, self.renderer.width - 230, self.renderer.height - 50
        )

        fps_text = self.font.render_text(f"FPS: {fps}", "main", (255, 0, 0))
        self.renderer.screen.blit(fps_text, (50, 100))
