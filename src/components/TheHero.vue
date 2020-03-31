/*
 * Created on Tue Mar 31 2020 by Johnathan Irvin
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

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
