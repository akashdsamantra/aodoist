<script>
  import { onMount, getContext } from "svelte";
  import Modal from "svelte-simple-modal";

  onMount(() => {});

  const { open } = getContext("simple-modal");

  const showSurprise = () => {
    open(Surprise, { message: "It's a modal!" });
  };
</script>

<Modal>
  <p><button on:click={showSurprise}>Show me a surprise!</button></p>
</Modal>
