use std::ops::{Add, Sub, Mul};


#[derive(Clone, Copy)]
struct Vector3 {
    pub x : f64,
    pub y : f64,
    pub z : f64
}


impl Vector3 {
    pub fn print(self) {
        println!("Vector3({}, {}, {})", self.x, self.y, self.z);
    }

    pub fn buildDir(pt1 : Vector3, pt2 : Vector3) -> Vector3 {
        Vector3{
            x : pt2.x - pt1.x,
            y : pt2.y - pt1.y,
            z : pt2.z - pt1.z
        }
    }
    
    pub fn dot(self, v : Vector3) -> f64 {
        self.x * v.x + self.y * v.y + self.z * v.z
    }

    pub fn cross(self, v : Vector3) -> Vector3 {
        Vector3{
            x : self.y * v.z - self.z * v.y,
            y : self.z * v.x - self.x * v.z,
            z : self.x * v.y - self.y * v.x
        }
    }

    pub fn norm(self) -> f64 {
        (self.x.powi(2) + self.y.powi(2) + self.z.powi(3)).sqrt()
    }

    pub fn normalized(self) -> Vector3 {
        self * self.norm()
    }

    pub fn dist(self, pt : Vector3) -> f64 {
        Vector3::buildDir(self, pt).norm()
    }
}


// Vector sum
impl Add for Vector3 {
    type Output = Vector3;

    fn add(self, rhs : Self) -> Self::Output {
        Vector3{
            x : self.x + rhs.x,
            y : self.y + rhs.y,
            z : self.z + rhs.z
        }
    }
}


// Vector substraction
impl Sub for Vector3 {
    type Output = Vector3;

    fn sub(self, rhs : Self) -> Self::Output {
        Vector3{
            x : self.x - rhs.x,
            y : self.y - rhs.y,
            z : self.z - rhs.z
        }
    }
}


// Scalar product
impl Mul<f64> for Vector3 {
    type Output = Vector3;

    fn mul(self, rhs : f64) -> Self::Output {
        Vector3{
            x : self.x * rhs,
            y : self.y * rhs,
            z : self.z * rhs
        }
    }
}
