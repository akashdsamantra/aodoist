<script>
    import PageLoader from "./components/PageLoader.svelte";

    export const isPageLoading = false;
</script>

<main>
    <PageLoader loading={isPageLoading} />
</main>
