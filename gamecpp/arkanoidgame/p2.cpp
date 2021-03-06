#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

using namespace std;
using namespace sf;

// 'constexpr' defines an immutable compile-time value
constexpr int windowWidth{800}, windowHeight{600};
constexpr float ballRadius{10.f};

// class for our ball
// struct == class in c++
struct Ball {
	// CircleShape is a SFML class that defines a renderable circle
	CircleShape shape;

	// constructor
	Ball(float mX, float mY) {
		// Apply pos, radius, color, origin
		shape.setPosition(mX, mY);
		shape.setRadius(ballRadius);
		shape.setFillColor(Color::Red);
		shape.setOrigin(ballRadius, ballRadius);
	}
};

int main() {

	// create instance of ball
	// positioned at the center of the window
	Ball ball(windowWidth / 2, windowHeight / 2);

	// Creation of the game window
	RenderWindow window{{windowWidth, windowHeight}, "Arkanoid - 1"};
	window.setFramerateLimit(60);

	// Game loop
	while(true) {

		// "Clear" the window from prev drawn graphics
		window.clear(Color::Black);
		// in some OS:
		// Event event;
		// window.pollEvent(event);

		// If "escape" is pressed, break loop
		if(Keyboard::isKeyPressed(Keyboard::Key::Escape)) break;

		// show the window contents
		window.draw(ball.shape);
		window.display();
	}

	return 0;
}