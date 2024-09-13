# catalog-template
Template for creating eodash catalog repository.

## How-to
You can create a new repository using the "use this template" button.
This will set-up a catalog repository for you with example configuration files as well as a github workflow that will automatically build and deploy the STAC catalog to the gh-page branch.
For every commit you push to the main branch the catalog will be regenerated and deployed there.

Please consider! This deployment strategy is intended for reasonable sized catalogs, if a catalog gets larger a more robust strategy should be implemented, changing the current github action, for example deploying the build to an s3 bucket.

To make the build catalog available through github pages, please go to:
 * repository settings
   - Pages (left side panel)
     - Source: "Deploy from branch" (should be selected)
     - Branch: Select "gh-pages" from dropdown
     - (leave root selected)
     - Click on save

Once enabled you can navigate to the catalog using:

https://\<organization\>.github.io/\<repository\>/\<catalog_name\>/catalog.json
