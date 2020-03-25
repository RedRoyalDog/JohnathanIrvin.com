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
        context: null
      }
    }
  },
  provide () {
    return {
      provider: this.provider
    }
  },

  mounted () {
    this.provider.context = this.$refs['base-canvas'].getContext('2d')

    this.$refs['base-canvas'].width = this.$refs['base-canvas'].parentElement.clientWidth
    this.$refs['base-canvas'].height = this.$refs['base-canvas'].parentElement.clientHeight
  }
}
</script>