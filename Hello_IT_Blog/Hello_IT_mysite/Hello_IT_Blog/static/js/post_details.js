//Post-details
const PostDetailsAnimation = () => {
  const postDetail = document.querySelector("#postDetail");
  const PostMore = () => {
    const postDetailsMore = document.querySelector("#postDetailsMore");
    const postMoreAnimation = anime.timeline({
      autoplay: true,
    });
    postMoreAnimation.add({
      targets: postDetailsMore,
      translateY: ["-100", "0"],
      opacity: [0, 1],
      duration: 900,
      easing: "easeOutSine",
    });
  };
  const postDetails = anime.timeline({
    autoplay: true,
  });
  postDetails.add({
    targets: postDetail,
    translateX: ["-100", "0"],
    opacity: [0, 1],
    duration: 600,
    easing: "easeOutSine",
    update(anim) {
      console.log(Math.round(anim.progress));
      if (Math.round(anim.progress) === 61) {
        PostMore();
      }
    },
  });
};

PostDetailsAnimation();
