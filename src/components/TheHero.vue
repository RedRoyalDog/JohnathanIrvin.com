<template lang="pug">
  b-jumbotron.fullheight(
      header="Johnathan Irvin"
      lead="Senior Software Engineer, Journalist, Entrepreneur, Creator, Inventor"
      bg-variant="dark"
      text-variant="light"
      fluid)
</template>

<script>
import TheNavBar from "../components/TheNavBar";

export default {
  name: "TheHero",
  components: {
    TheNavBar
  }
};
</script>

<style lang="css" scoped>
.fullheight.jumbotron {
  position: relative;
  background: url(../assets/img1.jpg) no-repeat center center;
  background-size: cover;
  min-height: 100%;  /* Fallback for browsers do NOT support vh unit */
  min-height: calc(100vh - 56px);
  margin-bottom: 0;
  display: flex;
  align-items: center;
  text-align: center;
  overflow:hidden
}
</style>
