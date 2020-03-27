export { Particle }

class Particle {
  constructor(x = 0, y = 0, speed = Math.random() * 0.9, directionAngle = Math.floor(Math.random() * 360)) {
    this.x = x;
    this.y = y;
    this.speed = speed;
    this.directionAngle = directionAngle;
    this.vector = {
      x: Math.cos(this.directionAngle) * this.speed,
      y: Math.sin(this.directionAngle) * this.speed,
    };
  }

  update() {
    this.x += this.vector.x;
    this.y += this.vector.y;
  }
}
