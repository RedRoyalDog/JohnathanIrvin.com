<template lang="pug">
    b-carousel(
        id="carousel-skills",
        v-model="slide",
        @sliding-start="onSlideStart",
        @sliding-end="onSlideEnd",
        img-width="1024",
        img-height="1024",
        :interval="4000",
    )
        b-carousel-slide.text-dark(
            img-blank,
        )
            h3.text-dark Front End
</template>

<script>
export default {
    name: "CarouselSkills",
    data() {
        return {
            slide: 0,
            sliding: null
        }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    },
}
</script>

<style scoped>

</style>