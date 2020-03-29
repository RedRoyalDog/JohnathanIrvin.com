<template lang="pug">
  b-jumbotron.fullheight#home(
      bg-variant="transparent"
      text-variant="light"
      fluid)
        TextType.relative.hero(slot='header', text='Johnathan Irvin')
        p.relative(slot='lead', style='z-index: 100') Senior Software Engineer, Journalist, Entrepreneur, Creator, Inventor
        BaseCanvas.fill(style='z-index: 99')
          CanvasParticle
</template>

<script>
import TheNavBar from '../components/TheNavBar';
import BaseCanvas from '../components/BaseCanvas';
import CanvasParticle from '../components/CanvasParticle';
import TextType from '../components/TextType'

export default {
  name: 'TheHero',
  components: {
    TheNavBar,
    BaseCanvas,
    CanvasParticle,
    TextType
  },
};
</script>

<style lang="css" scoped>
.hero { 
  z-index: 100;
  font-family: monospace;
  /* https://superuser.com/questions/361297/what-colour-is-the-dark-green-on-old-fashioned-green-screen-computer-displays */
  color: #33FF33;

  -webkit-animation: glow 1s ease-in-out infinite alternate;
  -moz-animation: glow 1s ease-in-out infinite alternate;
  animation: glow 1s ease-in-out infinite alternate;
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
  min-height: calc(100vh - 56px);
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
</style>
