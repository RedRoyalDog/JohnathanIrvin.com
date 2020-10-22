/*
 * Created on Thu Aug 27 2020 by Johnathan Irvin
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
module.exports = {
	siteName: 'Johnathan Irvin',
	siteUrl: 'https://johnathanirvin.com',
	siteDescription: 'Johnathan Irvin\'s portfolio. Engineer, Journalist, Entrepreneur.',
	icon: './src/favicon.jpg',
	plugins: [
		{
			use: 'gridsome-plugin-pug'
		},
		{
			use: '@gridsome/source-filesystem',
			options: {
				typeName: 'Post',
				path: 'src/blog/**/*.md',
			},
			refs: {
				tags: {
					typeName: 'Tag',
					create: true
				}
			},
			remark: {
				plugins: [
				  '@gridsome/remark-prismjs'
				]
			}
		},
		{
			use: '@gridsome/plugin-google-analytics',
			options: {
			id: 'UA-113451037-1'
			}
		},
		{
			use: 'gridsome-plugin-rss',
			options: {
				contentTypeName: 'Post',
				feedOptions: {
					title: 'Johnathan Irvin | Blog',
					feed_url: 'https://johnathanirvin.com/rss.xml',
					site_url: 'https://johnathanirvin.com/'
				},
				feedItemOptions: node => ({
					title: node.title,
					description: node.summary,
					url: 'https://johnathanirvin.com' + node.path,
					author: 'Johnathan Irvin',
					date: node.date
				}),
				output: {
					dir: './static',
					name: 'rss.xml'
				}
			}
		},
		{
			use: '@gridsome/plugin-sitemap',
			options: {
				cacheTime: 600000,
				config: {
					'/articles/*': {
						changefreq: 'weekly',
						priority: 0.5,
					}
				}
			}
		}
	],
	transformers: {
		remark: {
			plugins: [
				'remark-toc',
				'@gridsome/remark-prismjs'
			]
		}
	},
	templates: {
		Post: [
			{
				path: '/articles/:year/:month/:day/:title',
			},
			{
				name: 'redirects',
				path: '/articles/:title',
				component: './src/components/Redirect.vue'
			}
		]
	}
}
