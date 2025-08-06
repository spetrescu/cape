<script lang="ts">
	import { WEBUI_BASE_URL } from '$lib/constants';

	export let className = 'size-8';
	export let src = `${WEBUI_BASE_URL}/cape-icon.png`;
</script>

<img
	crossorigin="anonymous"
	src={
		src === ''
			? `${WEBUI_BASE_URL}/cape-icon.png`
			: src.startsWith(WEBUI_BASE_URL) ||
			  src.startsWith('https://www.gravatar.com/avatar/') ||
			  src.startsWith('data:') ||
			  src.startsWith('/')
			? src
			: `${WEBUI_BASE_URL}/cape-icon.png`
	}
	class="{className} object-cover rounded-full"
	alt="profile"
	draggable="false"
/>
