/*
 * Created on Wed Oct 14 2020 by Johnathan Irvin
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

 <template></template>

<script>
export default {
  metaInfo() {
    return {
        title: `Redirecting to ${this.$page.post.path}`,
        meta: [
            { 'http-equiv': 'refresh', content: `0; URL=${this.$page.post.path}`}
        ],
        link: [
            { rel: 'canonical', href: `https://johnathanirvin.com${this.$page.post.path}` }
        ]
    }
  }
}
</script>

<page-query>
query Redirect ($id: ID!) {
  post: post (id: $id) {
    path
  }
}
</page-query>