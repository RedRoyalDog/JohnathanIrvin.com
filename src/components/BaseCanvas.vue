<template lang="pug">
  div
    canvas(ref="base-canvas")
    slot
</template>

<script>
export default {
  data() {
    return {
      provider: {
        context: null,
        width: null,
        height: null
      },
    };
  },
  provide() {
    return {
      provider: this.provider
    };
  },
  methods: {
      resize() {
        this.provider.width = this.$refs['base-canvas'].parentElement.clientWidth;
        this.provider.height = this.$refs['base-canvas'].parentElement.clientHeight;

        this.$refs['base-canvas'].width = this.provider.width;
        this.$refs['base-canvas'].height = this.provider.height;
      }
  },
  mounted() {
    this.provider.context = this.$refs['base-canvas'].getContext('2d');

    this.resize();

    window.addEventListener('resize', this.resize.bind(this));
  },
};
</script>
