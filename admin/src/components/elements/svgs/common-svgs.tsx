import Image from "next/image";

const imageNameToSvg = {
  minus: "/svg/minus-icon.svg",
  plus: "/svg/plus-icon.svg",
  minusHover: "/svg/minus-icon-hover.svg",
  plusHover: "/svg/plus-icon-hover.svg",
};
type props = {
  imageName: keyof typeof imageNameToSvg;
  alt: string;
  height?: string | number;
  width?: string | number;
  layout?: "fixed" | "fill" | "intrinsic" | "responsive";
};
function CommonSvgs({ imageName, alt, height, width, layout }: props) {
  return (
    <Image
      src={imageNameToSvg[imageName]}
      alt={alt ?? ""}
      width={width}
      height={height}
      layout={!width && !height ? "fill" : layout ?? "fixed"}
    />
  );
}

export default CommonSvgs;
