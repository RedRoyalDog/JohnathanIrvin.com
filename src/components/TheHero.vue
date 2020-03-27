<template lang="pug">
  b-jumbotron.fullheight#home(
      header="Johnathan Irvin"
      lead="Senior Software Engineer, Journalist, Entrepreneur, Creator, Inventor"
      bg-variant="dark"
      text-variant="light"
      fluid)
        BaseCanvas.fill
          CanvasParticle
</template>

<script>
import TheNavBar from '../components/TheNavBar';
import BaseCanvas from '../components/BaseCanvas';
import CanvasParticle from '../components/CanvasParticle';

export default {
  name: 'TheHero',
  components: {
    TheNavBar,
    BaseCanvas,
    CanvasParticle,
  },
};
</script>

<style lang="css" scoped>
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
  overflow:hidden
}

.fullheight.jumbotron::after {
  content: "";
  background: url(../assets/img1.jpg) no-repeat center center;
  background-size: cover;
  background-attachment: fixed;
  opacity: 0.2;

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
