#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
//uniform sampler2d u_texture_0
//multiple texture by the ambient
uniform vec3 camPos;

vec3 getLight(vec3 color) {

    vec3 Normal = normalize(normal);
    //ambient
    vec3 ambient = light.Ia;
    //diffuse
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    //spectacular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 spectacular = spec * light.Is;



    return color * ambient + diffuse + spectacular;
}

void main () {
    float gamma = 2.2;
    //vec3 color = texture(u_texture_0, uv_0).rgb;
   // color = pow(color, vec3(gamma));
    vec3 color = vec3(uv_0, 0);
    color = getLight(color);

    color = pow(color, 1 /vec3(gamma));
    fragColor = vec4(color, 1.0);
}