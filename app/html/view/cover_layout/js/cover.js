// swiper module init
const carouselModule = (() => {
  return {
    configure: () => {
      const mySwiper = new Swiper('.swiper-container', {
        loop: true,
        speed: 2000,
        autoplay: true,
        pagenation: {
          el: ".swiper-pagenation",
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
      });
    },
  }
})

carouselModule.configure()
