<script>
import { Particle } from "../assets/js/particle";

function distance(x1, y1, x2, y2) {
    let dx = x1 - x2;
    let dy = y1 - y2;

    return Math.sqrt(dx**2 + dy**2)
}

export default {
  inject: ['provider'],
  created() {
      this._particles = [];
  },

  data() {
    return {
        particleDistance: 120,
        particleCount: 75,
        width: 0,
        height: 0,
        ctx: null,
        _particles: null,
        drawing: false
    };
  },

  methods: {
    _initialize() {
        this._particles = []
        for (var i = 0; i < this.particleCount; i++) {
            let x = Math.random() * this.width, y = Math.random() * this.height;
            this._particles.push(new Particle(x=x, y=y));
        }
    },

    _drawLink(particle, drawCtx) {
        for(const p of this._particles) {
            const d = distance(particle.x, particle.y, p.x, p.y);

            if (d > this.particleDistance) {
                continue;
            }

            const opacity = 0.8 - (d / this.particleDistance) * 0.8;
            drawCtx.strokeStyle = 'green';
            drawCtx.globalAlpha = opacity;
            drawCtx.beginPath();
            drawCtx.moveTo(particle.x, particle.y);
            drawCtx.lineTo(p.x, p.y);
            drawCtx.closePath();
            drawCtx.stroke();
            drawCtx.globalAlpha = 1;
        }
    },

    _draw() {
        try {
            this.ctx.clearRect(0, 0, this.width, this.height);
            this._particles.forEach(particle => {
                this.update(particle);
                this._drawLink(particle, this.ctx);
            })
        } catch (e) {
            throw e;
        }
    },

    _boundaryCheck(particle) {
        let x = particle.x, y = particle.y;

        if (x > this.width || x < 0) { 
            particle.vector.x *= -1;
            particle.x = Math.max(0, Math.min(this.width, x));
        }

        if (y > this.height || y < 0) {
            particle.vector.y *= -1;
            particle.y = Math.max(0, Math.min(this.height, y));
        }
    },

    update(p) {
        p.update();
        this._boundaryCheck(p);
    },

    _renderLoop() {
        requestAnimationFrame(this._renderLoop.bind(this));
        this._draw();
    }
  },

  render() {
    if (!this.provider.context) return;
    this.ctx = this.provider.context;
    this.width = this.provider.width;
    this.height = this.provider.height;

    if (!this.drawing) {
    this._initialize();
    this._renderLoop();
        this.drawing = true;
    }
  },
};
</script>