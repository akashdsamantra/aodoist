<script>
    import { onMount, getContext } from "svelte";
    import Template from "./Template.svelte";

    const { open } = getContext("simple-modal");

    export let message;

    onMount(() => {
        open(Template, { message });
    });
</script>
