import { OrbitControls } from "@react-three/drei";
import { Avatar } from "./Avatar";
import { useThree } from "@react-three/fiber";
import { useEffect } from "react";
import { Vector3 } from "three";

export const Experience = () => {
  const { camera } = useThree();
  
  useEffect(() => {
    camera.position.set(0, -3, 2);
  }, [camera]);

  return (
    <>
      <OrbitControls 
        enablePan={false}
        enableZoom={false}
        enableRotate={false}
      />
      <group position={[1.5, 0, -1]}>
        <Avatar />
      </group>
      <ambientLight intensity={1} />
    </>
  );
};