/*
 * Created on Mon Jul 13 2020 by Johnathan Irvin
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
.container
  h1.display-3.pb-3.mb-3.text-right
    u {{ title }}
  .row.border-bottom(
      v-for="post in posts"
      :key="post.id"
  ).post: .col
    div: h2 {{ post.title }}
    div.mb-1.text-muted {{ post.date }}
    div.mb-4: p.lead {{ post.description }}
    div.mb-4
      router-link.font-weight-bold.text-uppercase.text-primary(
        :to="post.path"
      ) Read more
</template>

<script>
export default {
  name: "BlogFeed",
  props: [
      'title'
  ],
  computed: {
    posts: function() {
      return this.$page.allPost.edges.map(item => item.node)
    }
  }
}
</script>

<style lang="scss">
.post { 
  z-index: 4;
  position: relative;
}
</style>