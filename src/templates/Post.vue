/*
 * Created on Tue Oct 13 2020 by Johnathan Irvin
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
Layout
  .container.article(style="min-height: 80vh; position: relative").pt-4
    h1.article-title {{ $page.post.title }}
    p.article-date {{ $page.post.date }} · #[i {{$page.post.timeToRead}} min read]
    article(v-html="$page.post.content").markdown
</template>

<script lang="ts">
export default {
    name: "Post"
}
</script>

<page-query>
query Post ($path: String!) {
  metadata {
    siteName
    siteDescription
  }
  post: post (path: $path) {
    id
    title
    content
    date (format: "D MMMM YYYY")
    timeToRead
  }
}
</page-query>

<style lang="scss">
.markdown img {
  background-color: #fff;
  box-sizing: content-box;
  max-width: 100%;
  margin: 0 auto; 
}

.markdown p {
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
}
</style>