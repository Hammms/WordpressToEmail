const axios = require('axios').default;

const cheerio = require('cheerio');

const getListings = (count = 5) => {
  return new Promise((resolve, reject) => {
    axios
      .get(
        `https://deathcarejobs.com/wp-json/wp/v2/job_listing?per_page=${count}&_fields=id,title,link,content,meta`
      )
      .then((response) => {
        let data = response.data;

        let listings = [];

        for (let i = 0; i < data.length; i++) {
          const listing = data[i];

          listings.push({
            title: listing.title.rendered,
            link: listing.link,
            company: listing.meta['_company_name'],
            location: listing.meta['_job_location'],
            application: listing.meta['_application'],
            excerpt:
              listing.meta['_job_excerpt'] !== ''
                ? listing.meta['_job_excerpt']
                : cheerio
                    .load(listing.content.rendered || '')('p:first')
                    .text()
                    .trim()
                    .substr(0, 175) + '...',
          });
        }

        resolve(listings);
      })
      .catch((err) => {
        reject(err);
      });
  });
};

module.exports.getListings = getListings;
