# Three.js 초급 개발자 가이드 (CDN 방식)

## 목차
1. [Three.js 소개](#threejs-소개)
2. [기본 HTML 구조 준비](#기본-html-구조-준비)
3. [Three.js CDN 불러오기](#threejs-cdn-불러오기)
4. [기본 3요소 이해하기](#기본-3요소-이해하기)
5. [Scene (장면) 만들기](#scene-장면-만들기)
6. [Camera (카메라) 설정하기](#camera-카메라-설정하기)
7. [Renderer (렌더러) 설정하기](#renderer-렌더러-설정하기)
8. [첫 번째 도형: 정육면체 만들기](#첫-번째-도형-정육면체-만들기)
9. [도형에 재질 적용하기](#도형에-재질-적용하기)
10. [애니메이션 추가하기](#애니메이션-추가하기)
11. [조명 추가하기](#조명-추가하기)
12. [다양한 도형 실습](#다양한-도형-실습)
13. [전체 코드 예제](#전체-코드-예제)

---

## Three.js 소개

**Three.js란?**
- Three.js는 웹 브라우저에서 3D 그래픽을 쉽게 구현할 수 있게 해주는 JavaScript 라이브러리입니다.
- WebGL을 기반으로 하며, 복잡한 WebGL 코드를 간단하게 작성할 수 있도록 도와줍니다.

**Three.js의 3가지 핵심 요소:**
1. **Scene (장면)**: 모든 3D 객체를 담는 컨테이너
2. **Camera (카메라)**: 장면을 보는 시점
3. **Renderer (렌더러)**: 장면을 실제로 화면에 그려주는 역할

---

## 기본 HTML 구조 준비

### 1. index.html 파일 생성

가장 먼저 기본적인 HTML 구조를 만듭니다.

**파일**: `index.html`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Three.js 시작하기</title>
    <style>
        /* 기본 스타일 설정 */
        body {
            margin: 0;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }

        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Three.js 캔버스가 여기에 추가됩니다 -->

    <!-- Three.js CDN을 여기에 추가할 예정 -->
</body>
</html>
```

**설명:**
- `margin: 0`: 브라우저 기본 여백 제거
- `overflow: hidden`: 스크롤바 숨김
- `canvas { display: block }`: 캔버스 요소의 기본 여백 제거

---

## Three.js CDN 불러오기

### 1. CDN 링크 추가

Three.js를 사용하기 위해 CDN 링크를 추가합니다.

**index.html 수정** (`</body>` 태그 바로 위에 추가):

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Three.js 시작하기</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }

        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Three.js CDN 불러오기 -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

    <script>
        // 여기에 Three.js 코드를 작성합니다
        console.log('Three.js가 로드되었습니다!');
        console.log('Three.js 버전:', THREE.REVISION);
    </script>
</body>
</html>
```

**설명:**
- `three.min.js`: Three.js 라이브러리의 압축된 버전
- `console.log()`: 브라우저 개발자 도구 콘솔에서 Three.js가 정상적으로 로드되었는지 확인
- 브라우저에서 F12를 눌러 개발자 도구를 열고 Console 탭에서 메시지를 확인할 수 있습니다

---

## 기본 3요소 이해하기

Three.js로 3D 장면을 만들기 위해서는 반드시 다음 3가지가 필요합니다:

### 1. Scene (장면)
```javascript
const scene = new THREE.Scene();
```
- 모든 3D 객체(도형, 조명, 카메라 등)를 담는 컨테이너
- 영화 세트장이라고 생각하면 됩니다

### 2. Camera (카메라)
```javascript
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
```
- 장면을 보는 시점을 결정
- 영화 촬영 카메라라고 생각하면 됩니다

### 3. Renderer (렌더러)
```javascript
const renderer = new THREE.WebGLRenderer();
```
- 카메라가 본 장면을 실제로 화면에 그려주는 역할
- 영화 프로젝터라고 생각하면 됩니다

**비유:**
- Scene = 무대/세트장
- Camera = 촬영 카메라
- Renderer = 영상을 화면에 보여주는 프로젝터

---

## Scene (장면) 만들기

### 1. Scene 생성

**코드:**
```javascript
// Scene 생성
const scene = new THREE.Scene();

// Scene의 배경색 설정 (선택사항)
scene.background = new THREE.Color(0x222222); // 어두운 회색
```

**설명:**
- `new THREE.Scene()`: 새로운 장면 객체 생성
- `scene.background`: 배경색 설정 (16진수 컬러 코드 사용)
  - `0x222222`: 어두운 회색
  - `0xffffff`: 흰색
  - `0x000000`: 검은색
  - `0x87ceeb`: 하늘색

**전체 코드:**
```html
<script>
    // Scene 생성
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    console.log('Scene이 생성되었습니다!');
</script>
```

---

## Camera (카메라) 설정하기

### 1. PerspectiveCamera 생성

**코드:**
```javascript
// Camera 생성
const camera = new THREE.PerspectiveCamera(
    75,                                    // FOV (Field of View, 시야각)
    window.innerWidth / window.innerHeight, // 종횡비 (Aspect Ratio)
    0.1,                                   // Near (가까운 클리핑 평면)
    1000                                   // Far (먼 클리핑 평면)
);

// 카메라 위치 설정
camera.position.z = 5; // z축으로 5만큼 뒤로 이동
```

**파라미터 설명:**

1. **FOV (Field of View, 시야각)**: `75`
   - 카메라가 볼 수 있는 범위 (각도)
   - 일반적으로 45~75 사이 값 사용
   - 값이 클수록 더 넓은 범위를 볼 수 있음 (광각 효과)

2. **Aspect Ratio (종횡비)**: `window.innerWidth / window.innerHeight`
   - 화면의 가로 세로 비율
   - 일반적으로 브라우저 창 크기 사용

3. **Near (가까운 클리핑 평면)**: `0.1`
   - 카메라로부터 이 거리보다 가까운 객체는 렌더링되지 않음
   - 너무 작으면 깜빡임 현상 발생 가능

4. **Far (먼 클리핑 평면)**: `1000`
   - 카메라로부터 이 거리보다 먼 객체는 렌더링되지 않음
   - 성능 최적화를 위해 적절한 값 설정

**카메라 위치 설정:**
```javascript
camera.position.x = 0;  // x축 위치 (좌우)
camera.position.y = 0;  // y축 위치 (상하)
camera.position.z = 5;  // z축 위치 (앞뒤)
```

**전체 코드:**
```html
<script>
    // Scene 생성
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    // Camera 생성
    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 5;

    console.log('Camera가 생성되었습니다!');
    console.log('카메라 위치:', camera.position);
</script>
```

---

## Renderer (렌더러) 설정하기

### 1. WebGLRenderer 생성

**코드:**
```javascript
// Renderer 생성
const renderer = new THREE.WebGLRenderer({
    antialias: true  // 안티앨리어싱 활성화 (더 부드러운 렌더링)
});

// 렌더러 크기 설정 (브라우저 창 크기에 맞춤)
renderer.setSize(window.innerWidth, window.innerHeight);

// 렌더러의 캔버스를 HTML body에 추가
document.body.appendChild(renderer.domElement);
```

**설명:**
- `antialias: true`: 계단 현상을 줄여 더 부드러운 그래픽 생성
- `setSize()`: 렌더러의 출력 크기 설정
- `renderer.domElement`: 렌더러가 생성한 `<canvas>` 요소
- `appendChild()`: 생성된 캔버스를 HTML에 추가

### 2. 반응형 설정 (선택사항)

브라우저 창 크기가 변경될 때 자동으로 조정되도록 설정:

```javascript
// 윈도우 리사이즈 이벤트 처리
window.addEventListener('resize', () => {
    // 카메라 종횡비 업데이트
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    // 렌더러 크기 업데이트
    renderer.setSize(window.innerWidth, window.innerHeight);
});
```

**전체 코드:**
```html
<script>
    // Scene 생성
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    // Camera 생성
    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 5;

    // Renderer 생성
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // 반응형 설정
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    console.log('Renderer가 생성되었습니다!');
</script>
```

---

## 첫 번째 도형: 정육면체 만들기

### 1. Geometry (기하학 구조) 생성

**코드:**
```javascript
// BoxGeometry 생성 (정육면체의 형태)
const geometry = new THREE.BoxGeometry(1, 1, 1);
```

**파라미터:**
- 첫 번째: 가로(width) 크기
- 두 번째: 세로(height) 크기
- 세 번째: 깊이(depth) 크기

**예시:**
```javascript
const geometry1 = new THREE.BoxGeometry(1, 1, 1);    // 정육면체
const geometry2 = new THREE.BoxGeometry(2, 1, 1);    // 가로로 긴 직육면체
const geometry3 = new THREE.BoxGeometry(1, 3, 1);    // 세로로 긴 직육면체
```

### 2. Material (재질) 생성

**코드:**
```javascript
// MeshBasicMaterial 생성 (기본 재질)
const material = new THREE.MeshBasicMaterial({
    color: 0x00ff00  // 초록색
});
```

**색상 예시:**
```javascript
const redMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000 });    // 빨간색
const greenMaterial = new THREE.MeshBasicMaterial({ color: 0x00ff00 });  // 초록색
const blueMaterial = new THREE.MeshBasicMaterial({ color: 0x0000ff });   // 파란색
const yellowMaterial = new THREE.MeshBasicMaterial({ color: 0xffff00 }); // 노란색
```

### 3. Mesh (메쉬) 생성 및 Scene에 추가

**코드:**
```javascript
// Mesh 생성 (Geometry + Material)
const cube = new THREE.Mesh(geometry, material);

// Scene에 Mesh 추가
scene.add(cube);
```

**설명:**
- `Mesh`: Geometry(형태)와 Material(재질)을 결합한 3D 객체
- `scene.add()`: 생성한 객체를 장면에 추가

### 4. 렌더링하기

**코드:**
```javascript
// 장면을 렌더링
renderer.render(scene, camera);
```

**전체 코드:**
```html
<script>
    // Scene 생성
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    // Camera 생성
    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 5;

    // Renderer 생성
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // 정육면체 생성
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // 렌더링
    renderer.render(scene, camera);

    console.log('정육면체가 생성되었습니다!');
</script>
```

**결과:**
- 이제 브라우저에서 초록색 정육면체를 볼 수 있습니다!
- 하지만 아직 움직이지 않습니다.

---

## 도형에 재질 적용하기

Three.js에는 다양한 재질(Material)이 있습니다. 각 재질은 서로 다른 특성을 가지고 있습니다.

### 1. MeshBasicMaterial (기본 재질)

**특징:**
- 조명의 영향을 받지 않음
- 항상 같은 색으로 표시됨
- 가장 빠르고 간단함

**코드:**
```javascript
const material = new THREE.MeshBasicMaterial({
    color: 0x00ff00,
    wireframe: false  // true로 설정하면 와이어프레임(뼈대)만 표시
});
```

### 2. MeshStandardMaterial (표준 재질)

**특징:**
- 조명의 영향을 받음
- 더 사실적인 렌더링
- 금속성(metalness)과 거칠기(roughness) 설정 가능

**코드:**
```javascript
const material = new THREE.MeshStandardMaterial({
    color: 0x00ff00,
    metalness: 0.5,  // 0: 비금속, 1: 완전 금속
    roughness: 0.5   // 0: 매끄러움, 1: 거침
});
```

### 3. MeshPhongMaterial (광택 재질)

**특징:**
- 조명의 영향을 받음
- 반짝이는 효과(specular) 표현 가능

**코드:**
```javascript
const material = new THREE.MeshPhongMaterial({
    color: 0x00ff00,
    shininess: 100,          // 광택 정도
    specular: 0x222222       // 반사광 색상
});
```

### 4. 재질 옵션들

**공통 옵션:**
```javascript
const material = new THREE.MeshBasicMaterial({
    color: 0x00ff00,         // 색상
    wireframe: true,         // 와이어프레임 모드
    transparent: true,       // 투명도 활성화
    opacity: 0.5,            // 투명도 (0: 완전투명, 1: 불투명)
    side: THREE.DoubleSide   // 양면 렌더링
});
```

**실습 예제:**
```html
<script>
    // ... 이전 코드 ...

    // 다양한 재질 테스트
    const material = new THREE.MeshBasicMaterial({
        color: 0xff6347,      // 토마토색
        wireframe: false       // 와이어프레임 끄기
    });

    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    renderer.render(scene, camera);
</script>
```

---

## 애니메이션 추가하기

정지된 도형을 회전시켜 애니메이션 효과를 만들어봅시다.

### 1. 애니메이션 함수 만들기

**코드:**
```javascript
// 애니메이션 함수
function animate() {
    // 다음 프레임에 이 함수를 다시 호출
    requestAnimationFrame(animate);

    // 큐브 회전시키기
    cube.rotation.x += 0.01;  // x축 회전
    cube.rotation.y += 0.01;  // y축 회전

    // 장면 렌더링
    renderer.render(scene, camera);
}

// 애니메이션 시작
animate();
```

**설명:**
- `requestAnimationFrame()`: 브라우저에게 다음 프레임에 함수를 실행하도록 요청
- 일반적으로 초당 60회 실행 (60 FPS)
- `cube.rotation.x += 0.01`: x축으로 조금씩 회전
- 값이 클수록 빠르게 회전

### 2. 다양한 회전 효과

**한 축으로만 회전:**
```javascript
function animate() {
    requestAnimationFrame(animate);

    cube.rotation.y += 0.02;  // y축으로만 회전

    renderer.render(scene, camera);
}
```

**다른 속도로 회전:**
```javascript
function animate() {
    requestAnimationFrame(animate);

    cube.rotation.x += 0.005;  // x축: 느리게
    cube.rotation.y += 0.02;   // y축: 빠르게

    renderer.render(scene, camera);
}
```

### 3. 시간 기반 애니메이션

더 부드러운 애니메이션을 위해 시간을 사용할 수도 있습니다:

```javascript
function animate() {
    requestAnimationFrame(animate);

    // 시간 값 사용 (부드러운 애니메이션)
    const time = Date.now() * 0.001;  // 초 단위로 변환

    cube.rotation.x = time;
    cube.rotation.y = time * 0.5;

    renderer.render(scene, camera);
}
```

**전체 코드:**
```html
<script>
    // Scene, Camera, Renderer 생성
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 5;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // 정육면체 생성
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // 애니메이션 함수
    function animate() {
        requestAnimationFrame(animate);

        // 큐브 회전
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;

        // 렌더링
        renderer.render(scene, camera);
    }

    // 애니메이션 시작
    animate();

    console.log('애니메이션이 시작되었습니다!');
</script>
```

---

## 조명 추가하기

조명을 추가하면 더 사실적인 3D 효과를 만들 수 있습니다.

**주의:** `MeshBasicMaterial`은 조명의 영향을 받지 않습니다. 조명 효과를 보려면 `MeshStandardMaterial` 또는 `MeshPhongMaterial`을 사용해야 합니다!

### 1. AmbientLight (환경광)

**특징:**
- 모든 방향에서 균일하게 비추는 빛
- 그림자가 없음
- 전체적인 밝기 조절

**코드:**
```javascript
// 환경광 생성
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);
```

**파라미터:**
- 첫 번째: 빛의 색상 (0xffffff = 흰색)
- 두 번째: 빛의 강도 (0.0 ~ 1.0, 기본값 1)

### 2. DirectionalLight (방향광)

**특징:**
- 특정 방향에서 비추는 빛 (태양광과 유사)
- 그림자 생성 가능

**코드:**
```javascript
// 방향광 생성
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);  // 빛의 위치
scene.add(directionalLight);
```

### 3. PointLight (점광)

**특징:**
- 한 점에서 모든 방향으로 퍼지는 빛 (전구와 유사)
- 거리에 따라 밝기가 감소

**코드:**
```javascript
// 점광 생성
const pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(10, 10, 10);  // 빛의 위치
scene.add(pointLight);
```

**파라미터:**
- 첫 번째: 빛의 색상
- 두 번째: 빛의 강도
- 세 번째: 빛이 닿는 최대 거리

### 4. 조명과 재질 함께 사용하기

**전체 예제:**
```html
<script>
    // Scene, Camera, Renderer
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 5;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // 조명 추가
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(5, 5, 5);
    scene.add(directionalLight);

    // 정육면체 생성 (조명 효과를 받는 재질 사용)
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshStandardMaterial({
        color: 0x00ff00,
        metalness: 0.3,
        roughness: 0.4
    });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // 애니메이션
    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }

    animate();
</script>
```

---

## 다양한 도형 실습

Three.js는 정육면체 외에도 다양한 기본 도형을 제공합니다.

### 1. SphereGeometry (구)

**코드:**
```javascript
const geometry = new THREE.SphereGeometry(
    1,      // 반지름
    32,     // 가로 분할 수 (많을수록 부드러움)
    32      // 세로 분할 수
);
const material = new THREE.MeshStandardMaterial({ color: 0xff0000 });
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);
```

### 2. CylinderGeometry (원기둥)

**코드:**
```javascript
const geometry = new THREE.CylinderGeometry(
    1,      // 윗면 반지름
    1,      // 아랫면 반지름
    2,      // 높이
    32      // 둘레 분할 수
);
const material = new THREE.MeshStandardMaterial({ color: 0x0000ff });
const cylinder = new THREE.Mesh(geometry, material);
scene.add(cylinder);
```

### 3. ConeGeometry (원뿔)

**코드:**
```javascript
const geometry = new THREE.ConeGeometry(
    1,      // 밑면 반지름
    2,      // 높이
    32      // 둘레 분할 수
);
const material = new THREE.MeshStandardMaterial({ color: 0xffff00 });
const cone = new THREE.Mesh(geometry, material);
scene.add(cone);
```

### 4. TorusGeometry (도넛/토러스)

**코드:**
```javascript
const geometry = new THREE.TorusGeometry(
    1,      // 도넛 반지름
    0.4,    // 튜브 반지름
    16,     // 단면 분할 수
    100     // 둘레 분할 수
);
const material = new THREE.MeshStandardMaterial({ color: 0xff00ff });
const torus = new THREE.Mesh(geometry, material);
scene.add(torus);
```

### 5. PlaneGeometry (평면)

**코드:**
```javascript
const geometry = new THREE.PlaneGeometry(
    5,      // 가로 크기
    5       // 세로 크기
);
const material = new THREE.MeshStandardMaterial({
    color: 0xcccccc,
    side: THREE.DoubleSide  // 양면 렌더링
});
const plane = new THREE.Mesh(geometry, material);
plane.rotation.x = -Math.PI / 2;  // 90도 회전 (바닥처럼 보이게)
scene.add(plane);
```

### 6. 여러 도형 함께 배치하기

**전체 예제:**
```html
<script>
    // Scene, Camera, Renderer
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x222222);

    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.set(0, 3, 10);  // 카메라를 위쪽에서 보도록 조정
    camera.lookAt(0, 0, 0);         // 원점을 바라보게 설정

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // 조명
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(5, 10, 5);
    scene.add(directionalLight);

    // 1. 정육면체
    const cubeGeometry = new THREE.BoxGeometry(1, 1, 1);
    const cubeMaterial = new THREE.MeshStandardMaterial({ color: 0xff0000 });
    const cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
    cube.position.set(-3, 0, 0);  // 왼쪽에 배치
    scene.add(cube);

    // 2. 구
    const sphereGeometry = new THREE.SphereGeometry(0.7, 32, 32);
    const sphereMaterial = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
    const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
    sphere.position.set(0, 0, 0);  // 중앙에 배치
    scene.add(sphere);

    // 3. 원뿔
    const coneGeometry = new THREE.ConeGeometry(0.7, 1.5, 32);
    const coneMaterial = new THREE.MeshStandardMaterial({ color: 0x0000ff });
    const cone = new THREE.Mesh(coneGeometry, coneMaterial);
    cone.position.set(3, 0, 0);  // 오른쪽에 배치
    scene.add(cone);

    // 애니메이션
    function animate() {
        requestAnimationFrame(animate);

        // 각 도형 회전
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;

        sphere.rotation.y += 0.01;

        cone.rotation.z += 0.01;

        renderer.render(scene, camera);
    }

    animate();
</script>
```

---

## 전체 코드 예제

이제 배운 모든 내용을 종합한 완전한 예제를 만들어봅시다.

**파일**: `index1.html`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Three.js 종합 예제</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            font-family: Arial, sans-serif;
        }

        canvas {
            display: block;
        }

        #info {
            position: absolute;
            top: 10px;
            left: 10px;
            color: white;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div id="info">
        <h3>Three.js 종합 예제</h3>
        <p>왼쪽: 회전하는 정육면체</p>
        <p>중앙: 회전하는 구</p>
        <p>오른쪽: 회전하는 원뿔</p>
    </div>

    <!-- Three.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>

    <script>
        // ===== Scene 생성 =====
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a2e);

        // ===== Camera 생성 =====
        // PerspectiveCamera(시야각, 종횡비, 근거리, 원거리)
        const camera = new THREE.PerspectiveCamera(
            75,
            window.innerWidth / window.innerHeight,
            0.1,
            1000
        );
        // 주석
        // camera.position.set(x, y, z)
        // z축을 늘리면 멀어지고, 줄이면 가까워집니다.
        // y축을 늘리면 위로 올라가고, 줄이면 아래로 내려갑니다.
        // x축을 늘리면 오른쪽으로 이동하고, 줄이면 왼쪽으로 이동합니다.
        // camera.lookAt(x, y, z)
        // 카메라가 바라보는 방향을 설정합니다.
        // 한 번씩 수정을 해보세요.
        camera.position.set(0, 3, 10); // 카메라를 위쪽에서 보도록 조정
        camera.lookAt(0, 0, 0); // 원점을 바라보게 설정

        // ===== Renderer 생성 =====
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // ===== 조명 추가 =====
        // 환경광 (전체적인 밝기)
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
        scene.add(ambientLight);

        // 방향광 (그림자 효과)
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(10, 10, 5);
        scene.add(directionalLight);

        // 점광 (색상 효과)
        const pointLight = new THREE.PointLight(0x00ffff, 0.5, 50);
        pointLight.position.set(-5, 5, 5);
        scene.add(pointLight);

        // ===== 정육면체 생성 =====
        // THREE.BoxGeometry(가로, 세로, 깊이)
        // THREE.MeshStandardMaterial(재질 속성)
        // metalness: 금속성, roughness: 거칠기
        const cubeGeometry = new THREE.BoxGeometry(1.5, 1.5, 1.5);
        const cubeMaterial = new THREE.MeshStandardMaterial({
            color: 0xff6b6b,
            metalness: 0.3,
            roughness: 0.4
        });
        const cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
        cube.position.set(-4, 0, 0);
        scene.add(cube);

        // ===== 구 생성 =====
        // THREE.SphereGeometry(반지름, 가로 세그먼트 수, 세로 세그먼트 수)
        const sphereGeometry = new THREE.SphereGeometry(1, 32, 32);
        const sphereMaterial = new THREE.MeshStandardMaterial({
            color: 0x4ecdc4,
            metalness: 0.5,
            roughness: 0.2
        });
        const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);
        sphere.position.set(0, 0, 0);
        scene.add(sphere);

        // ===== 원뿔 생성 =====
        // THREE.ConeGeometry(반지름, 높이, 세그먼트 수)
        const coneGeometry = new THREE.ConeGeometry(1, 2, 32);
        const coneMaterial = new THREE.MeshStandardMaterial({
            color: 0xffe66d,
            metalness: 0.4,
            roughness: 0.3
        });
        const cone = new THREE.Mesh(coneGeometry, coneMaterial);
        cone.position.set(4, 0, 0);
        scene.add(cone);

        // ===== 바닥 평면 생성 =====
        const planeGeometry = new THREE.PlaneGeometry(20, 20);
        const planeMaterial = new THREE.MeshStandardMaterial({
            color: 0x2d3561,
            side: THREE.DoubleSide,
            roughness: 0.8
        });
        const plane = new THREE.Mesh(planeGeometry, planeMaterial);
        plane.rotation.x = -Math.PI / 2;
        plane.position.y = -2;
        scene.add(plane);

        // ===== 애니메이션 함수 =====
        function animate() {
            requestAnimationFrame(animate);

            // 정육면체 회전
            // 숫자를 변경해보세요.
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;

            // 구 회전
            sphere.rotation.y += 0.01;
            sphere.rotation.z += 0.005;

            // 원뿔 회전
            cone.rotation.y += 0.02;

            // 점광 움직이기 (원형 궤도)
            const time = Date.now() * 0.001;
            pointLight.position.x = Math.cos(time) * 8;
            pointLight.position.z = Math.sin(time) * 8;

            // 렌더링
            renderer.render(scene, camera);
        }

        // ===== 반응형 설정 =====
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        // ===== 애니메이션 시작 =====
        animate();

        console.log('Three.js 애플리케이션이 시작되었습니다!');
    </script>
</body>
</html>
```

**이 예제에는 다음이 포함되어 있습니다:**

1. Scene, Camera, Renderer 설정
2. 세 가지 조명 (AmbientLight, DirectionalLight, PointLight)
3. 세 가지 도형 (정육면체, 구, 원뿔)
4. 바닥 평면
5. 각 도형의 다른 회전 애니메이션
6. 움직이는 점광
7. 반응형 디자인
8. 정보 표시 UI

---

## 축하합니다!

이제 Three.js의 기본을 모두 배웠습니다!

**배운 내용:**
- Three.js CDN으로 라이브러리 불러오기
- Scene, Camera, Renderer의 개념과 생성
- 다양한 도형 만들기
- 재질(Material) 적용하기
- 조명 추가하기
- 애니메이션 만들기
- 반응형 설정하기

**다음 단계:**
- 마우스 상호작용 추가하기 (OrbitControls)
- 텍스처 매핑
- 그림자 효과
- 파티클 시스템
- 3D 모델 불러오기 (GLTF, OBJ)
- 후처리 효과

계속 연습하면서 멋진 3D 웹 경험을 만들어보세요!
