<template lang="pug">
  b-jumbotron.fullheight#home(
      bg-variant="transparent"
      text-variant="light"
      fluid)
    TextType.relative.hero.appleII(
      slot='header',
      :type-characters='titleTyping',
      text='Johnathan Irvin',
      @typed='swapTyping')
    TextType.appleII.relative.lead(
      slot='lead',
      :type-characters='leadTyping',
      text='Senior Software Engineer, Journalist, Entrepreneur, Creator, Inventor')
    BaseCanvas.fill(style='z-index: 99')
      CanvasParticle
    p.bottom-center: i.down
</template>

<script>
import BaseCanvas from '../components/BaseCanvas';
import CanvasParticle from '../components/CanvasParticle';
import TextType from '../components/TextType'

export default {
  name: 'TheHero',
  components: {
    BaseCanvas,
    CanvasParticle,
    TextType
  },
  data: function() {
    return {
      titleTyping: true,
      leadTyping: false
    }
  },
  methods: {
    swapTyping() {
      this.titleTyping = false;
      this.leadTyping = true;
    }
  }
};
</script>

<style lang="css" scoped>
.appleII {
  /* https://superuser.com/questions/361297/what-colour-is-the-dark-green-on-old-fashioned-green-screen-computer-displays */
  color: #33FF33;

  -webkit-animation: glow 1s ease-in-out infinite alternate;
  -moz-animation: glow 1s ease-in-out infinite alternate;
  animation: glow 1s ease-in-out infinite alternate;
}

.lead { 
  z-index: 100;
  font-family: monospace;
}

.hero { 
  z-index: 100;
  font-family: monospace;
}

@-webkit-keyframes glow {
  from {
    text-shadow: 0 0 1px #000, 0 0 1px #000, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33;
  }
  to {
    text-shadow: 0 0 2px #000, 0 0 2px #33FF33, 0 0 2px #33FF33, 0 0 2px #33FF33, 0 0 2px #33FF33, 0 0 2px #33FF33, 0 0 2px #33FF33;
  }
}

.relative {
  position: relative;
}

.fill {
  position: absolute;
  width: 100%;
  height: 100%;

  top: 0;
  left: 0;
}

.fullheight.jumbotron {
  position: relative;

  min-height: 100%;  /* Fallback for browsers do NOT support vh unit */
  min-height: 100vh;
  margin-bottom: 0;
  display: flex;
  align-items: center;
  text-align: center;
  overflow: hidden;

  background-color: black !important;
}

.fullheight.jumbotron::after {
  content: "";
  background: url(../assets/img1.jpg) no-repeat center center;
  background-size: cover;
  background-attachment: fixed;
  opacity: 0.39;

  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  position: absolute;
  z-index: 1;
}

.fullheight.jumbotron > .container {
  z-index: 2;
}

.bottom-center {
  position: absolute !important;
  bottom: 0;
  right: 50%;
}

.down {
  width: 10px;
  height: 10px;
  color: white;
  border: solid;
  border-top: none;
  border-left: none;
  display: inline-block;
  position: relative;
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);

  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes bounce {
  0%   {top: -5px}
  50%  {top: 5px}
  100% {top: -5px}
}
</style>
