/* данные клиники — всё, что нужно менять, лежит здесь */
window.CLINIC = {
  name: "Dinastiya Stom Clinic",
  phone: "+7 776 773 24 21",
  phoneRaw: "+77767732421",
  whatsapp: "77767732421",
  telegram: "dinastiyastomclinic",
  instagram: "dinastiyastomclinic",
  email: "dinastiyastomclinic@mail.ru",
  address: "Астана, проспект Туран, 34Б",
  hours: "Приём с 09:00, запись через WhatsApp",
  gis: "https://2gis.kz/astana/search/Dinastiya%20Stom%20Clinic",
  gisRating: "5.0",
  gisCount: "160",

  /* отзывы: вставлять сюда тексты, которые разрешено публиковать.
     пример записи (удалить и заменить своими):
     { name: "Имя А.", date: "октябрь 2026", rating: 5, text: "текст отзыва" }
     пока массив пуст, карточки не показываются, остаётся только рейтинг 2ГИС */
  reviews: [],

  /* команда: имя и должность можно оставить пустыми — подпись тогда скрывается.
     фото лежат в img/, порядок = порядок на сайте */
  team: [
    { photo: "img/doc-1.webp", name: "", role: "" },
    { photo: "img/doc-2.webp", name: "", role: "" },
    { photo: "img/doc-3.webp", name: "", role: "" },
    { photo: "img/doc-4.webp", name: "", role: "" },
    { photo: "img/doc-5.webp", name: "", role: "" }
  ]
};
