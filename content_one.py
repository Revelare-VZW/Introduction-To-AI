from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)

if __name__ == '__main__':
    # ffmpeg needed and miktex library (also in path)

    from manim.utils.file_ops import open_file as open_media_file
    # (in command line) py -m manim content_one.py SquareToCircle
    #scene = SquareToCircle()
    #scene.render(preview=True)
    #open_media_file(scene.renderer.file_writer.movie_file_path)

    scene2 = ManimCELogo()
    scene2
    scene2.render(preview=True)
    #open_media_file(scene2.renderer.file_writer.movie_file_path)
