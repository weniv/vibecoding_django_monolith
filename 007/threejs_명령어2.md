# Three.js 게임 개발 가이드 - 요리 아이템 수집 게임

## 목차
1. [게임 개요](#게임-개요)
2. [게임 구조 설계](#게임-구조-설계)
3. [카메라 설정 (탑뷰)](#카메라-설정-탑뷰)
4. [맵(게임 필드) 만들기](#맵게임-필드-만들기)
5. [플레이어 캐릭터 생성](#플레이어-캐릭터-생성)
6. [키보드 입력 처리](#키보드-입력-처리)
7. [플레이어 이동 구현](#플레이어-이동-구현)
8. [충돌 감지](#충돌-감지)
9. [아이템 생성 및 배치](#아이템-생성-및-배치)
10. [아이템 수집 로직](#아이템-수집-로직)
11. [점수 시스템](#점수-시스템)
12. [UI 표시](#ui-표시)
13. [전체 게임 코드](#전체-게임-코드)

---

## 게임 개요

**게임 이름**: 요리 아이템 수집 (Cooking Item Collector)

**게임 설명**:
- Overcooked 스타일의 탑뷰 3D 게임
- 3명의 플레이어가 동시에 플레이
- 맵을 돌아다니며 요리 아이템을 수집
- 각 플레이어는 다른 색상으로 표시
- 아이템을 많이 수집한 플레이어가 승리

**조작 방법**:
- **플레이어 1 (빨강)**: W, A, S, D
- **플레이어 2 (파랑)**: 화살표 키 (↑, ←, ↓, →)
- **플레이어 3 (초록)**: I, J, K, L

**게임 요소**:
- 3D 맵 (바닥 + 벽)
- 3명의 플레이어 캐릭터 (요리사)
- 수집 가능한 요리 아이템 (토마토, 양파, 당근 등)
- 점수 표시 UI
- 타이머 (선택사항)

---

## 게임 구조 설계

### 1. 기본 구조

```javascript
// 게임 상태 관리
const gameState = {
    players: [],        // 플레이어 배열
    items: [],          // 아이템 배열
    walls: [],          // 벽 배열
    isRunning: true     // 게임 실행 상태
};

// 플레이어 데이터 구조
const player = {
    mesh: null,         // Three.js Mesh 객체
    position: { x: 0, z: 0 },  // 위치
    speed: 0.1,         // 이동 속도
    score: 0,           // 점수
    color: 0xff0000     // 색상
};

// 아이템 데이터 구조
const item = {
    mesh: null,         // Three.js Mesh 객체
    position: { x: 0, z: 0 },  // 위치
    type: 'tomato',     // 아이템 타입
    points: 10          // 점수
};
```

### 2. 게임 루프

```javascript
function gameLoop() {
    requestAnimationFrame(gameLoop);

    // 1. 입력 처리
    handlePlayerInput();

    // 2. 게임 로직 업데이트
    updatePlayers();
    checkCollisions();

    // 3. 렌더링
    renderer.render(scene, camera);
}
```

---

## 카메라 설정 (탑뷰)

### 1. 탑뷰 카메라 설정

Overcooked처럼 위에서 내려다보는 시점을 만듭니다.

**코드:**
```javascript
// 카메라 생성 (탑뷰)
const camera = new THREE.PerspectiveCamera(
    60,                                    // FOV
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

// 카메라를 위쪽에 배치하고 아래를 향하게 설정
camera.position.set(0, 20, 15);  // 위쪽, 약간 뒤쪽
camera.lookAt(0, 0, 0);           // 중심을 바라봄
```

**설명:**
- `position.y = 20`: 카메라를 위쪽에 배치
- `position.z = 15`: 약간 뒤쪽에 배치하여 각도 조절
- `lookAt(0, 0, 0)`: 맵의 중심을 바라보도록 설정

### 2. OrthographicCamera 사용 (선택사항)

더 정확한 탑뷰를 원한다면 OrthographicCamera를 사용할 수 있습니다.

**코드:**
```javascript
const aspect = window.innerWidth / window.innerHeight;
const frustumSize = 20;

const camera = new THREE.OrthographicCamera(
    -frustumSize * aspect / 2,  // left
    frustumSize * aspect / 2,   // right
    frustumSize / 2,            // top
    -frustumSize / 2,           // bottom
    0.1,                        // near
    1000                        // far
);

camera.position.set(0, 20, 0);
camera.lookAt(0, 0, 0);
```

---

## 맵(게임 필드) 만들기

### 1. 바닥 생성

**코드:**
```javascript
// 바닥 생성
function createFloor() {
    const floorGeometry = new THREE.PlaneGeometry(20, 20);
    const floorMaterial = new THREE.MeshStandardMaterial({
        color: 0xcccccc,
        side: THREE.DoubleSide
    });
    const floor = new THREE.Mesh(floorGeometry, floorMaterial);
    floor.rotation.x = -Math.PI / 2;  // 바닥이 수평이 되도록 회전
    floor.position.y = 0;
    scene.add(floor);

    return floor;
}
```

**설명:**
- `PlaneGeometry(20, 20)`: 20x20 크기의 평면
- `rotation.x = -Math.PI / 2`: 90도 회전하여 바닥으로 만듦

### 2. 벽 생성

**코드:**
```javascript
// 벽 생성 함수
function createWall(x, y, z, width, height, depth) {
    const geometry = new THREE.BoxGeometry(width, height, depth);
    const material = new THREE.MeshStandardMaterial({
        color: 0x8b4513  // 갈색
    });
    const wall = new THREE.Mesh(geometry, material);
    wall.position.set(x, y, z);
    scene.add(wall);

    // 충돌 감지를 위해 저장
    gameState.walls.push(wall);

    return wall;
}

// 맵 경계 벽 생성
function createBoundaryWalls() {
    const wallHeight = 2;
    const wallThickness = 0.5;
    const mapSize = 20;

    // 북쪽 벽
    createWall(0, wallHeight/2, -mapSize/2, mapSize, wallHeight, wallThickness);

    // 남쪽 벽
    createWall(0, wallHeight/2, mapSize/2, mapSize, wallHeight, wallThickness);

    // 서쪽 벽
    createWall(-mapSize/2, wallHeight/2, 0, wallThickness, wallHeight, mapSize);

    // 동쪽 벽
    createWall(mapSize/2, wallHeight/2, 0, wallThickness, wallHeight, mapSize);
}
```

### 3. 장애물 벽 추가

**코드:**
```javascript
// 맵 내부 장애물 생성
function createObstacles() {
    // 중앙 카운터
    createWall(0, 1, 0, 4, 2, 2);

    // 왼쪽 테이블
    createWall(-5, 0.5, -5, 2, 1, 2);

    // 오른쪽 테이블
    createWall(5, 0.5, 5, 2, 1, 2);
}
```

---

## 플레이어 캐릭터 생성

### 1. 플레이어 생성 함수

**코드:**
```javascript
// 플레이어 생성 함수
function createPlayer(x, z, color, controls) {
    // 플레이어 외형 (원기둥 = 요리사 모자)
    const bodyGeometry = new THREE.CylinderGeometry(0.5, 0.5, 1, 16);
    const bodyMaterial = new THREE.MeshStandardMaterial({ color: color });
    const body = new THREE.Mesh(bodyGeometry, bodyMaterial);
    body.position.set(x, 0.5, z);
    scene.add(body);

    // 모자 (원뿔)
    const hatGeometry = new THREE.ConeGeometry(0.6, 0.8, 16);
    const hatMaterial = new THREE.MeshStandardMaterial({ color: 0xffffff });
    const hat = new THREE.Mesh(hatGeometry, hatMaterial);
    hat.position.set(x, 1.4, z);
    scene.add(hat);

    // 플레이어 데이터 생성
    const player = {
        body: body,
        hat: hat,
        position: { x: x, z: z },
        speed: 0.15,
        score: 0,
        color: color,
        controls: controls,  // 키 설정
        velocity: { x: 0, z: 0 }
    };

    gameState.players.push(player);
    return player;
}
```

**설명:**
- `CylinderGeometry`: 원기둥으로 요리사 몸통 표현
- `ConeGeometry`: 원뿔로 요리사 모자 표현
- 각 플레이어는 body와 hat 두 개의 mesh를 가짐

### 2. 3명의 플레이어 생성

**코드:**
```javascript
// 플레이어 3명 생성
function createPlayers() {
    // 플레이어 1 (빨강) - WASD
    createPlayer(-5, -5, 0xff6b6b, {
        up: 'w', down: 's', left: 'a', right: 'd'
    });

    // 플레이어 2 (파랑) - 화살표
    createPlayer(5, -5, 0x4ecdc4, {
        up: 'arrowup', down: 'arrowdown',
        left: 'arrowleft', right: 'arrowright'
    });

    // 플레이어 3 (초록) - IJKL
    createPlayer(0, 5, 0x95e1d3, {
        up: 'i', down: 'k', left: 'j', right: 'l'
    });
}
```

---

## 키보드 입력 처리

### 1. 키 상태 추적

**코드:**
```javascript
// 키 입력 상태 저장
const keys = {};

// 키보드 이벤트 리스너
window.addEventListener('keydown', (event) => {
    keys[event.key.toLowerCase()] = true;
});

window.addEventListener('keyup', (event) => {
    keys[event.key.toLowerCase()] = false;
});
```

**설명:**
- `keys` 객체에 현재 눌린 키를 저장
- `keydown`: 키를 누르면 true
- `keyup`: 키를 떼면 false
- `toLowerCase()`: 대소문자 구분 없이 처리

### 2. 플레이어별 입력 처리

**코드:**
```javascript
// 플레이어 입력 처리
function handlePlayerInput(player) {
    player.velocity.x = 0;
    player.velocity.z = 0;

    // 위쪽 이동
    if (keys[player.controls.up]) {
        player.velocity.z = -player.speed;
    }

    // 아래쪽 이동
    if (keys[player.controls.down]) {
        player.velocity.z = player.speed;
    }

    // 왼쪽 이동
    if (keys[player.controls.left]) {
        player.velocity.x = -player.speed;
    }

    // 오른쪽 이동
    if (keys[player.controls.right]) {
        player.velocity.x = player.speed;
    }
}
```

---

## 플레이어 이동 구현

### 1. 플레이어 위치 업데이트

**코드:**
```javascript
// 플레이어 이동 업데이트
function updatePlayer(player) {
    // 입력 처리
    handlePlayerInput(player);

    // 새로운 위치 계산
    const newX = player.position.x + player.velocity.x;
    const newZ = player.position.z + player.velocity.z;

    // 충돌 체크
    if (!checkWallCollision(newX, newZ)) {
        // 충돌이 없으면 이동
        player.position.x = newX;
        player.position.z = newZ;

        // Mesh 위치 업데이트
        player.body.position.x = newX;
        player.body.position.z = newZ;
        player.hat.position.x = newX;
        player.hat.position.z = newZ;
    }
}

// 모든 플레이어 업데이트
function updatePlayers() {
    gameState.players.forEach(player => {
        updatePlayer(player);
    });
}
```

### 2. 대각선 이동 속도 조정

대각선으로 이동할 때 속도가 빨라지는 것을 방지:

**코드:**
```javascript
function handlePlayerInput(player) {
    player.velocity.x = 0;
    player.velocity.z = 0;

    let moveX = 0;
    let moveZ = 0;

    if (keys[player.controls.up]) moveZ -= 1;
    if (keys[player.controls.down]) moveZ += 1;
    if (keys[player.controls.left]) moveX -= 1;
    if (keys[player.controls.right]) moveX += 1;

    // 대각선 이동 시 속도 정규화
    if (moveX !== 0 && moveZ !== 0) {
        const length = Math.sqrt(moveX * moveX + moveZ * moveZ);
        moveX /= length;
        moveZ /= length;
    }

    player.velocity.x = moveX * player.speed;
    player.velocity.z = moveZ * player.speed;
}
```

---

## 충돌 감지

### 1. AABB (Axis-Aligned Bounding Box) 충돌 감지

**코드:**
```javascript
// 충돌 감지 함수
function checkWallCollision(x, z) {
    const playerRadius = 0.5;  // 플레이어 반지름

    for (let wall of gameState.walls) {
        const wallBox = new THREE.Box3().setFromObject(wall);

        // 플레이어 경계 박스
        const playerBox = new THREE.Box3(
            new THREE.Vector3(x - playerRadius, 0, z - playerRadius),
            new THREE.Vector3(x + playerRadius, 1, z + playerRadius)
        );

        // 충돌 체크
        if (wallBox.intersectsBox(playerBox)) {
            return true;  // 충돌 발생
        }
    }

    return false;  // 충돌 없음
}
```

### 2. 원형 충돌 감지 (간단한 방법)

**코드:**
```javascript
// 원형 충돌 감지 (플레이어 간 충돌)
function checkPlayerCollision(player1, player2) {
    const dx = player1.position.x - player2.position.x;
    const dz = player1.position.z - player2.position.z;
    const distance = Math.sqrt(dx * dx + dz * dz);

    const minDistance = 1.0;  // 최소 거리

    return distance < minDistance;
}
```

---

## 아이템 생성 및 배치

### 1. 아이템 생성 함수

**코드:**
```javascript
// 아이템 타입 정의
const itemTypes = [
    { type: 'tomato', color: 0xff6347, points: 10 },
    { type: 'onion', color: 0xffd700, points: 15 },
    { type: 'carrot', color: 0xff8c00, points: 20 },
    { type: 'lettuce', color: 0x90ee90, points: 12 }
];

// 아이템 생성 함수
function createItem(x, z, itemType) {
    // 아이템 외형 (구)
    const geometry = new THREE.SphereGeometry(0.3, 16, 16);
    const material = new THREE.MeshStandardMaterial({
        color: itemType.color,
        emissive: itemType.color,
        emissiveIntensity: 0.3
    });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(x, 0.3, z);
    scene.add(mesh);

    // 아이템 데이터
    const item = {
        mesh: mesh,
        position: { x: x, z: z },
        type: itemType.type,
        points: itemType.points,
        collected: false
    };

    gameState.items.push(item);
    return item;
}
```

### 2. 랜덤 아이템 배치

**코드:**
```javascript
// 랜덤 위치에 아이템 생성
function spawnRandomItem() {
    const mapSize = 18;  // 맵 크기 (벽 안쪽)

    // 랜덤 위치 생성
    let x, z;
    let validPosition = false;

    while (!validPosition) {
        x = (Math.random() - 0.5) * mapSize;
        z = (Math.random() - 0.5) * mapSize;

        // 벽과 충돌하지 않는지 확인
        if (!checkWallCollision(x, z)) {
            validPosition = true;
        }
    }

    // 랜덤 아이템 타입 선택
    const randomType = itemTypes[Math.floor(Math.random() * itemTypes.length)];

    createItem(x, z, randomType);
}

// 여러 아이템 생성
function createInitialItems(count) {
    for (let i = 0; i < count; i++) {
        spawnRandomItem();
    }
}
```

### 3. 아이템 애니메이션

아이템이 회전하고 위아래로 움직이게 만들기:

**코드:**
```javascript
// 아이템 애니메이션
function animateItems() {
    const time = Date.now() * 0.001;

    gameState.items.forEach((item, index) => {
        if (!item.collected) {
            // 회전
            item.mesh.rotation.y += 0.02;

            // 위아래로 움직임
            item.mesh.position.y = 0.3 + Math.sin(time * 2 + index) * 0.1;
        }
    });
}
```

---

## 아이템 수집 로직

### 1. 아이템 수집 체크

**코드:**
```javascript
// 아이템 수집 체크
function checkItemCollection(player) {
    const collectionRadius = 0.8;  // 수집 거리

    gameState.items.forEach(item => {
        if (!item.collected) {
            const dx = player.position.x - item.position.x;
            const dz = player.position.z - item.position.z;
            const distance = Math.sqrt(dx * dx + dz * dz);

            if (distance < collectionRadius) {
                // 아이템 수집
                collectItem(player, item);
            }
        }
    });
}

// 아이템 수집 처리
function collectItem(player, item) {
    // 점수 추가
    player.score += item.points;

    // 아이템 제거
    item.collected = true;
    scene.remove(item.mesh);

    // UI 업데이트
    updateScoreUI();

    // 새 아이템 생성
    setTimeout(() => {
        spawnRandomItem();
    }, 1000);

    console.log(`Player collected ${item.type}! Score: ${player.score}`);
}

// 모든 플레이어의 수집 체크
function checkAllCollections() {
    gameState.players.forEach(player => {
        checkItemCollection(player);
    });
}
```

---

## 점수 시스템

### 1. 점수 추적

**코드:**
```javascript
// 플레이어 점수 가져오기
function getPlayerScore(playerIndex) {
    return gameState.players[playerIndex].score;
}

// 최고 점수 플레이어 찾기
function getLeadingPlayer() {
    let leadingPlayer = gameState.players[0];

    gameState.players.forEach(player => {
        if (player.score > leadingPlayer.score) {
            leadingPlayer = player;
        }
    });

    return leadingPlayer;
}
```

### 2. 게임 종료 조건

**코드:**
```javascript
// 목표 점수
const TARGET_SCORE = 100;

// 승리 체크
function checkWinCondition() {
    gameState.players.forEach((player, index) => {
        if (player.score >= TARGET_SCORE) {
            endGame(index);
        }
    });
}

// 게임 종료
function endGame(winnerIndex) {
    gameState.isRunning = false;

    const winner = gameState.players[winnerIndex];
    console.log(`Player ${winnerIndex + 1} wins with ${winner.score} points!`);

    // 승리 메시지 표시
    showWinnerMessage(winnerIndex + 1);
}
```

---

## UI 표시

### 1. HTML UI 요소

**HTML:**
```html
<div id="gameUI">
    <div id="scoreBoard">
        <div class="playerScore" id="player1Score">
            <span class="playerName">Player 1 (Red)</span>
            <span class="score">0</span>
        </div>
        <div class="playerScore" id="player2Score">
            <span class="playerName">Player 2 (Blue)</span>
            <span class="score">0</span>
        </div>
        <div class="playerScore" id="player3Score">
            <span class="playerName">Player 3 (Green)</span>
            <span class="score">0</span>
        </div>
    </div>
    <div id="controls">
        <h3>Controls</h3>
        <p>Player 1: W, A, S, D</p>
        <p>Player 2: Arrow Keys</p>
        <p>Player 3: I, J, K, L</p>
    </div>
</div>
```

### 2. 점수 UI 업데이트

**JavaScript:**
```javascript
// 점수 UI 업데이트
function updateScoreUI() {
    gameState.players.forEach((player, index) => {
        const scoreElement = document.querySelector(
            `#player${index + 1}Score .score`
        );
        if (scoreElement) {
            scoreElement.textContent = player.score;
        }
    });
}
```

### 3. 승리 메시지

**JavaScript:**
```javascript
// 승리 메시지 표시
function showWinnerMessage(playerNumber) {
    const message = document.createElement('div');
    message.id = 'winnerMessage';
    message.innerHTML = `
        <h1>Player ${playerNumber} Wins!</h1>
        <p>Press R to restart</p>
    `;
    document.body.appendChild(message);

    // R 키로 재시작
    window.addEventListener('keydown', (event) => {
        if (event.key.toLowerCase() === 'r' && !gameState.isRunning) {
            location.reload();
        }
    });
}
```

---

## 전체 게임 코드

위의 모든 요소를 결합한 완전한 게임 코드는 `index2.html` 파일에 작성되어 있습니다.

### 게임 초기화 순서

```javascript
// 1. Scene, Camera, Renderer 설정
initScene();

// 2. 조명 추가
addLights();

// 3. 맵 생성
createFloor();
createBoundaryWalls();
createObstacles();

// 4. 플레이어 생성
createPlayers();

// 5. 아이템 생성
createInitialItems(10);

// 6. 게임 루프 시작
gameLoop();
```

### 게임 루프 구조

```javascript
function gameLoop() {
    requestAnimationFrame(gameLoop);

    if (gameState.isRunning) {
        // 플레이어 업데이트
        updatePlayers();

        // 아이템 애니메이션
        animateItems();

        // 충돌 체크
        checkAllCollisions();

        // 수집 체크
        checkAllCollections();

        // 승리 조건 체크
        checkWinCondition();
    }

    // 렌더링
    renderer.render(scene, camera);
}
```

---

## 추가 기능 아이디어

### 1. 타이머 추가

```javascript
let gameTime = 60;  // 60초

function updateTimer() {
    if (gameTime > 0) {
        gameTime -= 0.016;  // 약 60 FPS
        document.getElementById('timer').textContent =
            Math.ceil(gameTime);
    } else {
        endGameByTime();
    }
}
```

### 2. 파워업 아이템

```javascript
const powerUpTypes = [
    { type: 'speed', color: 0x00ffff, duration: 5000 },
    { type: 'double', color: 0xff00ff, duration: 10000 }
];

function applyPowerUp(player, powerUp) {
    if (powerUp.type === 'speed') {
        player.speed *= 1.5;
        setTimeout(() => {
            player.speed /= 1.5;
        }, powerUp.duration);
    }
}
```

### 3. 사운드 효과

```javascript
// Web Audio API 사용
const audioContext = new AudioContext();

function playCollectSound() {
    const oscillator = audioContext.createOscillator();
    oscillator.frequency.value = 800;
    oscillator.connect(audioContext.destination);
    oscillator.start();
    oscillator.stop(audioContext.currentTime + 0.1);
}
```

### 4. 미니맵

```javascript
// 작은 카메라로 전체 맵 보기
const minimapCamera = new THREE.OrthographicCamera(
    -10, 10, 10, -10, 0.1, 100
);
minimapCamera.position.set(0, 30, 0);
minimapCamera.lookAt(0, 0, 0);

// 별도 캔버스에 렌더링
const minimapRenderer = new THREE.WebGLRenderer();
minimapRenderer.setSize(200, 200);
minimapRenderer.render(scene, minimapCamera);
```

---

## Django 연동 준비

향후 Django와 연동할 때 필요한 요소들:

### 1. 게임 데이터 전송

```javascript
// 게임 결과를 서버로 전송
async function saveGameResult() {
    const gameData = {
        players: gameState.players.map(p => ({
            score: p.score,
            color: p.color
        })),
        duration: gameDuration,
        winner: getLeadingPlayer()
    };

    await fetch('/api/game/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(gameData)
    });
}
```

### 2. 실시간 멀티플레이어 (WebSocket)

```javascript
// WebSocket 연결
const socket = new WebSocket('ws://localhost:8000/ws/game/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    updateOtherPlayers(data);
};

function sendPlayerPosition(player) {
    socket.send(JSON.stringify({
        type: 'player_move',
        position: player.position
    }));
}
```

---

## 마무리

이제 Three.js를 사용한 3D 멀티플레이어 요리 아이템 수집 게임의 모든 핵심 요소를 배웠습니다!

**구현된 기능:**
- 탑뷰 3D 카메라
- 3명의 플레이어 동시 조작
- 키보드 입력 처리
- 플레이어 이동 및 충돌 감지
- 아이템 생성 및 수집
- 점수 시스템
- UI 표시

**다음 단계:**
- Django 백엔드 연동
- WebSocket을 통한 실시간 멀티플레이어
- 데이터베이스에 게임 기록 저장
- 리더보드 시스템
- 사용자 인증 및 프로필

`index2.html` 파일을 열어서 게임을 플레이해보세요!
